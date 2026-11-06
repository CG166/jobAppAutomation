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

Python takes the
