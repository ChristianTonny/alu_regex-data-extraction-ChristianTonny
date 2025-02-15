import re

class DataExtractor:
    def __init__(self):
        # Email pattern
        self.email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # URL pattern
        self.url_pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
        
        # Phone number pattern 
        self.phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]\d{4}'
        
        # Time pattern
        self.time_pattern = r'(?:(?:2[0-3]|[01]?[0-9]):[0-5][0-9](?:\s?[AaPp][Mm])?)|(?:1[0-2]|0?[1-9]):[0-5][0-9]\s?[AaPp][Mm]'
        
        # HTML tag pattern
        self.html_pattern = r'<[^>]+>'
        
        # Currency pattern
        self.currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
        
        # New patterns to add
        self.credit_card_pattern = r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}'
        self.hashtag_pattern = r'#[A-Za-z0-9_]+\b'

    def extract_emails(self, text):
        """Extract email addresses from text."""
        return re.findall(self.email_pattern, text)
    
    def extract_urls(self, text):
        """Extract URLs from text."""
        return re.findall(self.url_pattern, text)
    
    def extract_phone_numbers(self, text):
        """Extract phone numbers from text."""
        return re.findall(self.phone_pattern, text)
    
    def extract_times(self, text):
        """Extract time values from text."""
        return re.findall(self.time_pattern, text)
    
    def extract_html_tags(self, text):
        """Extract HTML tags from text."""
        return re.findall(self.html_pattern, text)
    
    def extract_currency(self, text):
        """Extract currency amounts from text."""
        return re.findall(self.currency_pattern, text)

    def extract_credit_cards(self, text):
        """Extract credit card numbers from text."""
        return re.findall(self.credit_card_pattern, text)
    
    def extract_hashtags(self, text):
        """Extract hashtags from text."""
        return re.findall(self.hashtag_pattern, text)

    def extract_all(self, text):
        """Extract all supported patterns from text."""
        return {
            'emails': self.extract_emails(text),
            'urls': self.extract_urls(text),
            'phone_numbers': self.extract_phone_numbers(text),
            'times': self.extract_times(text),
            'html_tags': self.extract_html_tags(text),
            'currency': self.extract_currency(text),
            'credit_cards': self.extract_credit_cards(text),
            'hashtags': self.extract_hashtags(text)
        }

# Test implementation
def test_extractor():
    extractor = DataExtractor()
    
    # Test text 
    test_text = """
    Contact us at user@example.com or firstname.lastname@company.co.uk
    Visit our website at https://www.example.com or http://subdomain.example.org/page
    Call us at (123) 456-7890 or 123-456-7890 or 123.456.7890
    Meeting times: 14:30 or 2:30 PM
    <div class="example">Hello</div>
    <img src="image.jpg" alt="description">
    Price: $19.99 or $1,234.56
    """
    
    # print results
    results = extractor.extract_all(test_text)
    
    print("Extraction Results:")
    for category, items in results.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for item in items:
            print(f"  - {item}")

if __name__ == "__main__":
    test_extractor()