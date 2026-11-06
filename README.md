# Job Application & Resume Generation Automation

A Python automation project that streamlines parts of the job application process by collecting job listings and generating customized PDF resumes using Playwright and LaTeX.

## Overview

Applying to multiple positions often involves repetitive tasks, such as collecting job information and preparing separate resume documents. This project automates two parts of that workflow:

1. **Job Listing Collection:** Uses Playwright to navigate a job listing platform, extract job titles and company information, and identify unique opportunities.
2. **Resume Generation:** Uses Python to populate a LaTeX resume template with position-specific and company-specific information, then compiles the template into a PDF.

The goal is to reduce repetitive manual work and make the application preparation process more efficient.

## Features

### Automated Job Listing Collection
- Uses Python and Playwright for browser automation.
- Navigates job listings and handles page scrolling.
- Extracts job titles and company names.
- Identifies unique opportunities to avoid duplicate listings.
- Collects information for further processing.

### Automated Resume Generation
- Uses a reusable LaTeX resume template.
- Replaces template placeholders with job-specific information:
  - `{{POSITION}}` — Target job title.
  - `{{COMPANY}}` — Company name.
- Handles special characters that require escaping in LaTeX.
- Compiles populated templates into PDF documents using `pdflatex`.
- Generates separate resume files for different opportunities.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Automation and data processing |
| Playwright | Browser automation and job listing extraction |
| LaTeX | Resume document formatting |
| pdflatex | Compiling LaTeX files into PDFs |

## How It Works

The workflow consists of two main stages:

**1. Collect Job Listings**

Playwright automates browser interactions to navigate job listings, extract relevant information, and identify unique opportunities.

**2. Generate Resume Documents**

Python takes the collected position and company information and inserts it into a LaTeX template. The resulting `.tex` document is compiled with `pdflatex` to produce a PDF resume.

```text
Job Listing Platform
        |
        v
   Playwright
        |
        v
 Extract Job Information
        |
        v
 Identify Unique Listings
        |
        v
   Python Script
        |
        v
 Populate LaTeX Template
        |
        v
      pdflatex
        |
        v
   Customized PDF
```

## Requirements

- Python 3
- Playwright for Python
- LaTeX distribution with `pdflatex`
- A supported browser installed through Playwright

## Setup

### 1. Install Python Dependencies

Install Playwright:

```bash
pip install playwright
```

Install the browser binaries:

```bash
playwright install chromium
```

### 2. Install LaTeX

On Ubuntu:

```bash
sudo apt update
sudo apt install texlive-latex-base
```

Verify the installation:

```bash
pdflatex --version
```

### 3. Configure the Project

Configure the browser automation and resume template paths according to your local project setup.

If the job listing platform requires authentication, use locally stored browser session cookies. Keep authentication files private and never commit cookies, credentials, or other sensitive information to GitHub.

## Usage

Run the Python automation script:

```bash
python jobbot.py
```

The script collects job information and passes the relevant position and company details to the resume generation workflow.

The generated PDF documents can then be reviewed before submitting applications.

## Security

This project may use browser session cookies to access authenticated job listings.

**Important:** Authentication cookies and session data should never be committed to version control or included in a public repository.

Use a `.gitignore` file to exclude sensitive files:

```gitignore
# Browser cookies and session data
cookies.json
*cookie*
*.cookie

# Environment variables and secrets
.env
.env.*

# Python
__pycache__/
*.pyc

# Generated files
generated_resumes/
*.log
```

## Future Improvements

- Expand support for additional job listing platforms.
- Improve job listing filtering and organization.
- Add support for additional resume templates.
- Automate more steps in the job application preparation workflow.
- Introduce configurable resume sections and formatting options.

## Author

**Cindy Garcia**

- GitHub: [CG166](https://github.com/CG166)
- LinkedIn: [Cindy Garcia](https://www.linkedin.com/in/cindy-garcia-ba1684247)
