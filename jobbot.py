import json
from playwright.sync_api import sync_playwright # type: ignore
import genres


#####Fetching cookies from cookies.json(exported with Cookie-editor chrome extension) and converting to Playwright format######
with open("cookies.json", "r") as f:
    raw_cookies = json.load(f)

# Convert Chrome format → Playwright format
cookies = []

for c in raw_cookies:
    cookie = {
        "name": c["name"],
        "value": c["value"],
        "domain": c["domain"],
        "path": c.get("path", "/"),
        "secure": c.get("secure", False),
        "httpOnly": c.get("httpOnly", False),
        "sameSite": c.get("sameSite", "Lax").capitalize(),
    }

    # Convert expirationDate → expires
    if "expirationDate" in c:
        cookie["expires"] = int(c["expirationDate"])

    cookies.append(cookie)
############################################################################################################

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()

    context.add_cookies(cookies)

    page = context.new_page()
    page.goto("https://jobright.ai/jobs/recommend")

    #page.wait_for_load_state("networkidle")

    print("Logged in successfully ✅")

    ####################Extract job titles and company names from job cards#############################
    seen_jobs = set()
    max_scrolls = 30
    scrolls = 0

    while scrolls < max_scrolls:

        page.wait_for_selector("h2[class*='index_job-title']")

        titles = page.locator("h2[class*='index_job-title']").all_inner_texts()
        companies = page.locator("div[class*='index_company-name']").all_inner_texts()

        new_found = 0

        for title, company in zip(titles, companies):
            job_key = f"{title}-{company}"

            if job_key not in seen_jobs:
                seen_jobs.add(job_key)
                print(f"{len(seen_jobs)}. {title} @ {company}")
                genres.generate_resume(
                    position=title,
                    company=company 
                )
                new_found += 1

        if new_found == 0:
            print("No new jobs loaded. Stopping.")
            break

        page.mouse.wheel(0, 5000)
        page.wait_for_timeout(1500)

        scrolls += 1

    print("Finished collecting jobs.")
    print("Total unique jobs:", len(seen_jobs))
    ###############################################################################################
