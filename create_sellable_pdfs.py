#!/usr/bin/env python3
"""
Create sellable PDFs for children's books
Properly combines text and illustrations
"""

from fpdf import FPDF
import os
import re

# Constants
INCH = 25.4
BOOK_WIDTH = 8 * INCH
BOOK_HEIGHT = 10 * INCH
MARGIN = 0.5 * INCH


def parse_manuscript(filepath):
    """Parse manuscript text file and extract pages"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pages = {}
    current_page = None
    current_text = ""
    
    for line in content.split('\n'):
        line = line.strip()
        
        # Check for page markers
        page_match = re.match(r'PAGE\s+(\d+(?:-\d+)?)', line)
        if page_match:
            if current_page:
                pages[current_page] = current_text.strip()
            current_page = page_match.group(1)
            current_text = ""
        elif line.startswith('==='):
            continue
        elif line.startswith('[') and line.endswith(']'):
            # Illustration description - skip
            continue
        else:
            current_text += line + "\n"
    
    if current_page:
        pages[current_page] = current_text.strip()
    
    return pages


def create_book_pdf(book_dir, book_title, manuscript_path):
    """Create a proper PDF for a book"""
    base_dir = f"/home/user/children_books/{book_dir}"
    ill_dir = os.path.join(base_dir, "illustrations")
    cover_dir = os.path.join(base_dir, "cover")
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Parse manuscript
    pages_text = parse_manuscript(manuscript_path)
    
    pdf = FPDF(unit="mm", format=(BOOK_WIDTH, BOOK_HEIGHT))
    pdf.set_auto_page_break(False)
    pdf.set_font("Helvetica", "", 12)
    
    # Add cover
    cover_path = os.path.join(cover_dir, "front_cover.png")
    if os.path.exists(cover_path):
        pdf.add_page()
        pdf.image(cover_path, 0, 0, BOOK_WIDTH, BOOK_HEIGHT)
    
    # Add title page
    title_path = os.path.join(ill_dir, "page_02_03_title.png")
    if os.path.exists(title_path):
        pdf.add_page()
        pdf.image(title_path, 0, 0, BOOK_WIDTH, BOOK_HEIGHT)
        # Add text
        pdf.set_xy(MARGIN, BOOK_HEIGHT/2 - 20)
        pdf.set_font("Helvetica", "B", 16)
        pdf.cell(0, 10, book_title, ln=True, align='C')
        pdf.set_font("Helvetica", "I", 14)
        pdf.cell(0, 10, "Written by", ln=True, align='C')
        pdf.cell(0, 10, "Hamidreza Rostami", ln=True, align='C')
    
    # Add copyright page
    pdf.add_page()
    pdf.set_font("Helvetica", "", 12)
    pdf.set_xy(MARGIN, BOOK_HEIGHT/2 - 30)
    pdf.cell(0, 8, book_title, ln=True, align='C')
    pdf.cell(0, 8, "Written by Hamidreza Rostami", ln=True, align='C')
    pdf.cell(0, 8, "", ln=True)
    pdf.cell(0, 8, "Copyright (c) 2026 Hamidreza Rostami", ln=True, align='C')
    pdf.cell(0, 8, "All rights reserved.", ln=True, align='C')
    pdf.cell(0, 8, "Buyer has usage rights only.", ln=True, align='C')
    
    # Add story pages
    # For each page with illustration, add the image and text
    for page_num in sorted(pages_text.keys(), key=lambda x: int(x.split('-')[0]) if '-' not in x else int(x.split('-')[0])):
        if page_num in ['1', '2-3', '4']:
            continue  # Already added
        
        # Find corresponding illustration
        ill_files = [f for f in os.listdir(ill_dir) if f.startswith(f"page_{page_num}")]
        
        pdf.add_page()
        
        if ill_files:
            ill_path = os.path.join(ill_dir, ill_files[0])
            pdf.image(ill_path, 0, 0, BOOK_WIDTH, BOOK_HEIGHT)
        
        # Add text
        text = pages_text.get(page_num, "")
        if text:
            pdf.set_font("Helvetica", "", 14)
            pdf.set_text_color(0, 0, 0)
            lines = text.split('\n\n')
            y = BOOK_HEIGHT - MARGIN - 20
            for line in lines:
                if line.strip():
                    pdf.set_xy(MARGIN, y)
                    pdf.multi_cell(BOOK_WIDTH - 2*MARGIN, 8, line, align='C')
                    y -= 10
    
    # Save PDF
    safe_title = book_title.replace(" ", "_").replace("'", "")
    pdf_path = os.path.join(pdf_dir, f"{safe_title}.pdf")
    pdf.output(pdf_path)
    print(f"  Created: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    books = [
        ("04_The_Day_the_Colors_Ran_Away", "The Day the Colors Ran Away", 
         "/home/user/children_books/04_The_Day_the_Colors_Ran_Away/manuscript/story.txt"),
        ("05_Captain_Whiskers_and_the_Great_Yarn_Adventure", "Captain Whiskers and the Great Yarn Adventure",
         "/home/user/children_books/05_Captain_Whiskers_and_the_Great_Yarn_Adventure/manuscript/story.txt"),
        ("06_The_Tiny_Giant", "The Tiny Giant",
         "/home/user/children_books/06_The_Tiny_Giant/manuscript/story.txt"),
    ]
    
    print("Creating sellable PDFs...")
    print("=" * 60)
    
    for book_dir, title, manuscript_path in books:
        print(f"\nProcessing: {title}")
        create_book_pdf(book_dir, title, manuscript_path)
    
    print("\n" + "=" * 60)
    print("PDF generation complete!")
