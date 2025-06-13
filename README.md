# Markdown to CSV Converter

A simple and efficient Python tool that converts markdown tables to CSV format. This tool is particularly useful for data migration, data analysis, or when you need to work with tabular data in different formats.

## Features

- Converts markdown tables to CSV format
- Removes markdown formatting lines (e.g., `|------|------|...`)
- Replaces `|` delimiters with commas (`,`)
- Maintains consistent column count across rows
- Preserves data integrity
- UTF-8 encoding support
- Simple command-line interface
- Automatic output filename generation

## Requirements

- Python 3.6 or higher
- pandas library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/markdown_to_csv.git
cd markdown_to_csv
```

2. Create and activate a virtual environment:

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
Convert a markdown file to CSV using the default output filename (same name with .csv extension):
```bash
python markdown_to_csv.py input_file.md
```

### Specify Output File
Convert a markdown file to CSV with a custom output filename:
```bash
python markdown_to_csv.py input_file.md output_file.csv
```

## Examples

### Example 1: Basic Table Conversion

Input markdown file (`example.md`):
```markdown
| Name | Age | City |
|------|-----|------|
| John | 25  | NY   |
| Mary | 30  | LA   |
```

Output CSV file (`example.csv`):
```csv
Name,Age,City
John,25,NY
Mary,30,LA
```

### Example 2: Complex Table Conversion

Input markdown file (`complex.md`):
```markdown
| Product | Price | Quantity | Category |
|---------|-------|----------|----------|
| Laptop  | 999   | 5        | Tech     |
| Phone   | 699   | 10       | Tech     |
| Book    | 19.99 | 100      | Books    |
```

Output CSV file (`complex.csv`):
```csv
Product,Price,Quantity,Category
Laptop,999,5,Tech
Phone,699,10,Tech
Book,19.99,100,Books
```

## Error Handling

The script includes error handling for common scenarios:
- File not found errors
- Permission errors
- Invalid file format errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository. 