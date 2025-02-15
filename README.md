# ALU Regex Data Extraction Project

## Overview
This project implements a data extraction tool using regular expressions to extract various types of information from text. 

## Features
The current implementation extracts the following data types:

1. **Email addresses** - Supports standard formats including those with subdomains
2. **URLs** - Supports both HTTP and HTTPS with various domain structures
3. **Phone numbers** - Supports multiple formats including parentheses, dots, and dashes
4. **Time** - Supports both 12-hour and 24-hour formats
5. **HTML tags** - Extracts complete tags including those with attributes
6. **Currency amounts** - Supports dollar amounts with optional commas and decimal places


### Installation
1. Clone this repository:
```
git clone https://github.com/ChristianTonny/alu_regex-data-extraction-christiantonny.git
cd alu_regex-data-extraction-christiantonny
```

2. No additional libraries are required as this project only uses Python's built-in `re` module.

### Basic Usage
```python
from data_extractor import DataExtractor

# Create an instance of the extractor
extractor = DataExtractor()

# Sample text containing various patterns
text = """
Contact us at user@example.com or firstname.lastname@company.co.uk
Visit our website at https://www.example.com or http://subdomain.example.org/page
Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890
Meeting times: 14:30 or 2:30 PM
<div class="example">Hello</div>
<img src="image.jpg" alt="description">
Price: $19.99 or $1,234.56
"""

# Extract all supported patterns
results = extractor.extract_all(text)

# Print results
for category, items in results.items():
    print(f"\n{category.replace('_', ' ').title()}:")
    for item in items:
        print(f"  - {item}")
```

### Extracting Specific Data Types
You can also extract specific data types:

```python
# Extract only emails
emails = extractor.extract_emails(text)
print("Emails:", emails)

# Extract only URLs
urls = extractor.extract_urls(text)
print("URLs:", urls)
```

## Regex Patterns Explained

### Email Pattern
`\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`
- Matches standard email formats
- Supports letters, numbers, and common special characters in the username
- Supports domain names with subdomains
- Requires a valid TLD of at least 2 characters

### URL Pattern
`https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)`
- Matches HTTP and HTTPS URLs
- Supports optional www prefix
- Captures domains with various TLDs
- Includes query parameters and paths

### Phone Number Pattern
`\(?\d{3}\)?[-.\s]?\d{3}[-.\s]\d{4}`
- Matches formats: (123) 456-7890, 123-456-7890, 123.456.7890
- Supports optional parentheses around area code
- Supports separation by dashes, dots, or spaces

### Time Pattern
`(?:(?:2[0-3]|[01]?[0-9]):[0-5][0-9](?:\s?[AaPp][Mm])?)|(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?[AaPp][Mm]`
- Matches both 24-hour format (14:30) and 12-hour format (2:30 PM)
- Handles optional leading zeros
- Case-insensitive AM/PM indicators

### HTML Tag Pattern
`<[^>]+>`
- Matches opening and closing HTML tags
- Supports tags with attributes
- Captures complete tag structure

### Currency Pattern
`\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?`
- Matches dollar amounts starting with $
- Supports optional thousands separators (commas)
- Supports optional decimal places (up to 2 digits)

## Testing
Run the included test function to verify the implementation:

```python
if __name__ == "__main__":
    test_extractor()
```


## Author
Christian Tonny
