import pytesseract
from PIL import Image
import re

def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    
    # Simple rules to extract metadata
    lines = text.split('\n')
    metadata = {'title': '', 'author': '', 'isbn': '', 'synopsis': '', 'keywords': ''}
    
    for line in lines:
        line = line.strip()
        if 'ISBN' in line:
            metadata['isbn'] = re.findall(r'\d+', line)[0] if re.findall(r'\d+', line) else ''
        elif 'Author' in line or 'author' in line:
            metadata['author'] = line.split(':')[-1].strip()
        elif len(line.split()) > 3:  # Assuming title is a longer line
            metadata['title'] = line.strip()
        # Add more rules as necessary
    
    # Synopsis and keywords might require more advanced NLP processing
    metadata['synopsis'] = 'Extracted synopsis text here'
    metadata['keywords'] = 'Extracted keywords here'
    
    return metadata
