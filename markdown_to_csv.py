#!/usr/bin/env python3

import sys
import pandas as pd
import re
from pathlib import Path

def clean_markdown_table(markdown_content):
    """Clean markdown table content by removing formatting lines and converting to CSV format."""
    # Split content into lines
    lines = markdown_content.strip().split('\n')
    
    # Remove markdown formatting lines (lines containing only | and -)
    cleaned_lines = [line for line in lines if not re.match(r'^\s*\|[\s\-:|]+\|\s*$', line)]
    
    # Convert | to commas
    csv_lines = [line.replace('|', ',').strip(',') for line in cleaned_lines]
    
    return '\n'.join(csv_lines)

def convert_markdown_to_csv(input_file, output_file=None):
    """Convert a markdown table file to CSV format."""
    try:
        # Read the markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Clean the markdown content
        csv_content = clean_markdown_table(markdown_content)
        
        # Generate output filename from input filename
        if output_file is None:
            input_path = Path(input_file)
            output_file = input_path.with_suffix('.csv')
        
        # Write the CSV content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(csv_content)
        
        print(f"Successfully converted {input_file} to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Could not find the input file '{input_file}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("Usage: python markdown_to_csv.py <input_file.md> [output_file.csv]")
        print("If output_file is not specified, it will use the input filename with .csv extension")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_markdown_to_csv(input_file, output_file)

if __name__ == "__main__":
    main() 