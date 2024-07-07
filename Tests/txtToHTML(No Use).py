import os
import sys

def read_text_file(file_path):
    """Read the content of a text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_html_file(content, output_file_path):
    """Write content wrapped in HTML tags to an HTML file."""
    html_content = '''
    <html>
    <head>
        <title>Converted HTML</title>
    </head>
    <body>
        <pre>{}</pre>
    </body>
    </html>'''.format(content)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

def main(input_file_path, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract the base name of the input file and set the output path
    base_name = os.path.basename(input_file_path)
    output_file_name = os.path.splitext(base_name)[0] + '.html'
    output_file_path = os.path.join(output_dir, output_file_name)
    
    # Read the text file
    content = read_text_file(input_file_path)
    
    # Write the HTML file
    write_html_file(content, output_file_path)
    print(f"HTML file has been written to {output_file_path}")

if __name__ == "__main__":
    # Example usage 
    # Replace 'path/to/your/textfile.txt' with actual path to the input text file
    # Replace 'output/directory/path' with actual path to the output directory

    input_file_path = 'path/to/your/textfile.txt'
    output_dir = 'output/directory/path'
    
    main(input_file_path, output_dir)