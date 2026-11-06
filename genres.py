import subprocess
from pathlib import Path
from datetime import datetime
import os
import re


def escape_tex(text: str) -> str:
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }

    for char, escaped_char in replacements.items():
        text = text.replace(char, escaped_char)

    return text



def generate_resume(position: str, company: str):
    """
    Generates a customized resume PDF by:
    1. Reading the LaTeX template
    2. Replacing placeholders with user input
    3. Writing a new .tex file
    4. Compiling it into a PDF using pdflatex
    """

    # ---- Paths ----
    # Path to your LaTeX template
    template_path = Path("resume_template.tex")

    # Folder where generated resumes will be stored
    output_dir = Path("generated_resumes")

    # Create the folder if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # ---- Read the template file ----
    latex_content = template_path.read_text()

    # ---- Escape LaTeX special characters ----
    safe_position = escape_tex(position)
    safe_company = escape_tex(company)

    # ---- Replace placeholders in template ----
    # Your template should contain:
    # {{POSITION}} and {{COMPANY}}
    latex_content = latex_content.replace("{{POSITION}}", safe_position)
    latex_content = latex_content.replace("{{COMPANY}}", safe_company)

    # ---- Create a clean filename ----
    # Remove spaces for cleaner filenames
    filename_company = re.sub(r'[<>:"/\\|?*\s]+', '_', company)
    filename_position = re.sub(r'[<>:"/\\|?*\s]+', '_', position)

    # Add date to prevent overwriting previous resumes
    #timestamp = datetime.now().strftime("%Y%m%d")

    # Final .tex file path
    output_tex = output_dir / f"{filename_company}_{filename_position}_Resume.tex"

    # Write modified LaTeX content to new file
    output_tex.write_text(latex_content)

    # ---- Compile LaTeX into PDF ----
    # This runs pdflatex from the terminal
    result = subprocess.run(
        ["pdflatex", "-output-directory", str(output_dir), str(output_tex)],
        check=True,
        stdout=subprocess.DEVNULL,  # ignore standard output
        stderr=subprocess.DEVNULL   # ignore error output
    )

    # Later, if needed:
    if result.returncode != 0:
        print("LaTeX compilation failed:")
        print(result.stderr)

    for ext in [".aux", ".log", ".out", ".tex"]:
        file_to_remove = output_tex.with_suffix(ext)
        if file_to_remove.exists():
            os.remove(file_to_remove)



    # Print final PDF location
    #print(f"\nResume generated successfully:")
    #print(output_tex.with_suffix(".pdf"))


# ----Example Usage----
#if __name__ == "__main__":
    #generate_resume(
        #position="Software Engineer",
        #company="liveramp"
    #)
