# Web Scraping - E-Commerce Product Data Extraction

This project is a web scraping tool that extracts product information such as names, prices, and ratings from an e-commerce website. The extracted data is stored in a structured format (CSV) for further analysis or use.

## Project Overview

The program scrapes product information from a specified e-commerce webpage (e.g., Flipkart). It retrieves the following details:
- Product Name
- Price
- Rating

This information is then saved in a CSV file, which can be easily accessed and analyzed.

## Features

- Scrapes product data from the provided URL.
- Extracts product names, prices, and ratings.
- Saves the scraped data to a CSV file.
- Can be easily modified for other e-commerce websites.

## Requirements

The following Python libraries are required to run this project:
- `requests`: To make HTTP requests and fetch the webpage content.
- `beautifulsoup4`: To parse HTML and extract product information.
- `pandas`: To store the extracted data in a CSV file.

You can install all required dependencies by running:

```bash
pip install -r requirements.txt
