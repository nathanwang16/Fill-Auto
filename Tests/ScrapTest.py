# -*- coding: utf-8 -*-
"""
Title: Webpage HTML Scraper
Author: Xiaoyu Wang (Nathan)
Description: This script navigates to a specified website, waits for it to fully load, and writes the complete HTML of the page to a text file. 
    The script receives variables from a yaml config file.
"""

#make sure to change the absolute path to relative path when pushing to Github

import yaml
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Copyright
# This script is part of a project by Xiaoyu Wang (Nathan)

def load_config(config_file):
    """Load configuration from a YAML file."""
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    # Load configuration
    config = load_config('/Users/wangxiaoyu/Desktop/Fill-Auto/Tests/url+dir.yaml')
    
    url = config['url']
    output_dir = config['output_dir']
    webdriver_path = config['webdriver_path']
    
    # Configure Chrome options to run in headless mode
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # Initialize the ChromeDriver with headless mode options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open the web page
        driver.get(url)

        # OPTIONAL: Wait for a specific element to be present before proceeding.
        try:
            element_present = EC.presence_of_element_located((By.TAG_NAME, 'body'))
            WebDriverWait(driver, 10).until(element_present)
        except Exception as e:
            print(f"Error waiting for page to load: {e}")

        # Get the page source (complete HTML)
        page_source = driver.page_source

        # Create output file with the name of the website
        output_filename = f"{url.split('//')[-1].split('/')[0]}.txt"
        output_path = os.path.join(output_dir, output_filename)

        # Write the HTML to a file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(page_source)
        print(f"Page source has been written to {output_path}")

    finally:
        # Clean up and close the WebDriver
        driver.quit()

if __name__ == "__main__":
    main()