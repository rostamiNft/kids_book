#!/usr/bin/env python3
"""
Final PDF Generator - Creates sellable PDFs with proper text and images
"""

from weasyprint import HTML
import os
import re

# Book list
BOOKS = [
    "04_The_Day_the_Colors_Ran_Away",
    "05_Captain_Whiskers_and_the_Great_Yarn_Adventure",
    "06_The_Tiny_Giant",
    "07_The_Quiet_Little_Drum",
    "08_The_Last_Leaf_of_Autumn",
    "09_The_Boy_Who_Painted_Dreams",
    "10_The_Little_Library_of_Lost_Things",
]


def extract_text_from_manuscript(filepath):
    """Extract text from manuscript, removing illustration descriptions"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    pages = {}
    current_page = None
    current_text = []
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines and separators
        if not line or line == '===' or line.startswith('==='):
            continue
        
        # Check for page marker
        page_match = re.match(r'PAGE\s+(\d+(?:-\d+)?)', line)
        if page_match:
            if current_page:
                pages[current_page] = '\n'.join(current_text).strip()
            current_page = page_match.group(1)
            current_text = []
            continue
        
        # Skip illustration descriptions
        if line.startswith('[') and line.endswith(']'):
            continue
        
        # Skip title lines in manuscript
        if 'by Hamidreza Rostami' in line:
            continue
        
        current_text.append(line)
    
    if current_page:
        pages[current_page] = '\n'.join(current_text).strip()
    
    return pages


def create_html(book_dir, title, pages_text):
    """Create HTML for a book"""
    ill_dir = os.path.join(book_dir, "illustrations")
    cover_dir = os.path.join(book_dir, "cover")
    
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  body { margin: 0; padding: 0; }
  .page { width: 8in; height: 10in; position: relative; page-break-after: always; background: white; }
  img { position: absolute; max-width: 8in; max-height: 10in; object-fit: contain; top: 0; left: 0; }
  .text { position: absolute; bottom: 0.5in; left: 0.5in; right: 0.5in; font-family: Georgia, serif; font-size: 16pt; line-height: 1.5; text-align: center; color: #333; }
  .title-text { font-size: 20pt; font-weight: bold; }
  .copyright-text { font-size: 12pt; line-height: 1.6; }
</style>
</head>
<body>
'''
    
    # Cover
    cover_path = os.path.join(cover_dir, "front_cover.png")
    if os.path.exists(cover_path):
        html += f'<div class="page"><img src="{cover_path}" style="width:8in;height:10in;object-fit:cover;"></div>\n'
    
    # Title page
    title_img = os.path.join(ill_dir, "page_02_03_title.png")
    if os.path.exists(title_img):
        html += f'<div class="page"><img src="{title_img}">\n'
        html += f'<div class="text title-text">{title}<br><br>Written by<br>Hamidreza Rostami</div></div>\n'
    
    # Copyright page
    html += '<div class="page"><div class="text copyright-text">'
    html += f'{title}<br><br>Written by Hamidreza Rostami<br><br>'
    html += 'Copyright (c) 2026 Hamidreza Rostami<br>All rights reserved.<br>Buyer has usage rights only.</div></div>\n'
    
    # Story pages
    for page_num in sorted(pages_text.keys(), key=lambda x: (int(x.split('-')[0]) if '-' not in x else int(x.split('-')[0]), 0 if '-' not in x else int(x.split('-')[1]))):
        if page_num in ['1', '2-3', '4']:
            continue
        
        html += '<div class="page">'
        
        # Find illustration
        ill_files = [f for f in os.listdir(ill_dir) if f.startswith(f"page_{page_num}")]
        if ill_files:
            html += f'<img src="{ill_dir}/{ill_files[0]}">'
        
        # Add text
        text = pages_text.get(page_num, "")
        if text:
            html += f'<div class="text">{text}</div>'
        
        html += '</div>\n'
    
    html += '</body></html>'
    return html


def create_pdf(book_dir, title):
    """Create PDF for a book"""
    manuscript_path = os.path.join(book_dir, "manuscript", "story.txt")
    pdf_dir = os.path.join(book_dir, "pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Extract text
    pages_text = extract_text_from_manuscript(manuscript_path)
    
    # Create HTML
    html = create_html(book_dir, title, pages_text)
    
    # Save and convert
    html_path = os.path.join(book_dir, "temp.html")
    with open(html_path, 'w') as f:
        f.write(html)
    
    pdf_path = os.path.join(pdf_dir, f"{title.replace(' ', '_')}.pdf")
    HTML(html_path, base_url=book_dir).write_pdf(pdf_path)
    
    os.remove(html_path)
    print(f"  ✓ Created: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    print("Creating final sellable PDFs...")
    print("=" * 60)
    
    book_titles = {
        "04_The_Day_the_Colors_Ran_Away": "The Day the Colors Ran Away",
        "05_Captain_Whiskers_and_the_Great_Yarn_Adventure": "Captain Whiskers and the Great Yarn Adventure",
        "06_The_Tiny_Giant": "The Tiny Giant",
        "07_The_Quiet_Little_Drum": "The Quiet Little Drum",
        "08_The_Last_Leaf_of_Autumn": "The Last Leaf of Autumn",
        "09_The_Boy_Who_Painted_Dreams": "The Boy Who Painted Dreams",
        "10_The_Little_Library_of_Lost_Things": "The Little Library of Lost Things",
    }
    
    for book_dir, title in book_titles.items():
        full_path = os.path.join("/home/user/children_books", book_dir)
        if os.path.exists(full_path):
            print(f"\nProcessing: {title}")
            create_pdf(full_path, title)
        else:
            print(f"\nSkipping: {title} (directory not found)")
    
    print("\n" + "=" * 60)
    print("All PDFs created!")
