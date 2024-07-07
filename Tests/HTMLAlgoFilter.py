# -*- coding: utf-8 -*-
"""
Title: Webpage HTML txt algorithm input field filter/finder
Author: Xiaoyu Wang (Nathan)
Description: It tries to find all input fields in a html field and print relative attributes.
"""


from bs4 import BeautifulSoup
import os

# Example function to read HTML content from a file
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

# Function to find input fields and extract context and attributes
def find_input_fields(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    input_fields = []

    # Find all input elements
    inputs = soup.find_all('input')
    
    for input_element in inputs:
        field_info = {}
        field_info['type'] = input_element.get('type', 'text')
        field_info['name'] = input_element.get('name')
        field_info['id'] = input_element.get('id')
        field_info['value'] = input_element.get('value')

        # Find the label, if any, associated with the input
        label = input_element.find_previous('label')
        if label:
            field_info['label'] = label.get_text()

        # Find surrounding context (e.g., sibling text)
        sibling_texts = []
        for sibling in input_element.next_siblings:
            if sibling.name:
                break
            if sibling.string and sibling.string.strip():
                sibling_texts.append(sibling.string.strip())
        field_info['context'] = ' '.join(sibling_texts)
        
        input_fields.append(field_info)

    return input_fields

# Function to display the input fields and their attributes
def display_input_fields(input_fields):
    for i, field in enumerate(input_fields):
        print(f"Input Field {i + 1}:")
        print(f"  Type    : {field['type']}")
        print(f"  Name    : {field['name']}")
        print(f"  ID      : {field['id']}")
        print(f"  Value   : {field['value']}")
        print(f"  Label   : {field.get('label', 'N/A')}")
        print(f"  Context : {field.get('context', 'N/A')}")
        print()

def main():
    # Path to the HTML file (update this path as needed)
    html_file_path = '/Users/wangxiaoyu/Desktop/Fill-Auto/Tests/ScrapTestOutput/artofproblemsolving.com.txt'
    
    # Read the HTML file
    html_content = read_html_file(html_file_path)
    
    # Find input fields and extract attributes and context
    input_fields = find_input_fields(html_content)
    
    # Display the input fields with their attributes and context
    display_input_fields(input_fields)

if __name__ == "__main__":
    main()