#!/usr/bin/env python3
"""
Script to create PDFs for children's books
Uses fpdf2 library to generate professional PDFs
"""

from fpdf import FPDF
import os

# Constants
BOOK_WIDTH = 8 * 25.4  # 8 inches in mm
BOOK_HEIGHT = 10 * 25.4  # 10 inches in mm
MARGIN = 12.7  # 0.5 inches in mm
FONT_FAMILY = "Helvetica"


def create_book_pdf(book_dir, book_title, author="Hamidreza Rostami"):
    """Create a PDF for a children's book"""
    pdf = FPDF(unit="mm", format=(BOOK_WIDTH, BOOK_HEIGHT))
    
    # Add cover
    cover_path = os.path.join(book_dir, "cover", "front_cover.png")
    if os.path.exists(cover_path):
        pdf.add_page()
        pdf.image(cover_path, 0, 0, BOOK_WIDTH, BOOK_HEIGHT)
    
    # Add title page
    title_page_path = os.path.join(book_dir, "illustrations", "page_02_03_title.png")
    if os.path.exists(title_page_path):
        pdf.add_page()
        pdf.image(title_page_path, 0, 0, BOOK_WIDTH, BOOK_HEIGHT)
        # Add text overlay
        pdf.set_font(FONT_FAMILY, 'B', 16)
        pdf.set_text_color(100, 100, 100)
        pdf.set_xy(MARGIN, BOOK_HEIGHT / 2 - 20)
        pdf.cell(0, 10, book_title, ln=True, align='C')
        pdf.set_font(FONT_FAMILY, 'I', 12)
        pdf.set_xy(MARGIN, BOOK_HEIGHT / 2 + 5)
        pdf.cell(0, 10, f"Written by\n{author}", ln=True, align='C')
    
    # Add copyright page
    pdf.add_page()
    pdf.set_font(FONT_FAMILY, '', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.set_xy(MARGIN, BOOK_HEIGHT / 2 - 30)
    pdf.cell(0, 8, book_title, ln=True, align='C')
    pdf.cell(0, 8, f"Written by {author}", ln=True, align='C')
    pdf.cell(0, 8, "", ln=True)
    pdf.cell(0, 8, "Copyright (c) 2026 Hamidreza Rostami", ln=True, align='C')
    pdf.cell(0, 8, "All rights reserved.", ln=True, align='C')
    pdf.cell(0, 8, "Buyer has usage rights only.", ln=True, align='C')
    
    # Add story pages
    illustrations_dir = os.path.join(book_dir, "illustrations")
    for filename in sorted(os.listdir(illustrations_dir)):
        if filename.endswith('.png') and filename != 'page_02_03_title.png' and filename != 'page_04_copyright.png':
            page_num = filename.replace('page_', '').replace('.png', '')
            # Skip pages we already added
            if page_num in ['02_03_title', '04_copyright']:
                continue
            
            pdf.add_page()
            img_path = os.path.join(illustrations_dir, filename)
            pdf.image(img_path, 0, 0, BOOK_WIDTH, BOOK_HEIGHT)
    
    # Save PDF
    pdf_dir = os.path.join(book_dir, "pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    pdf_path = os.path.join(pdf_dir, f"{book_title.replace(' ', '_')}_print.pdf")
    pdf.output(pdf_path)
    print(f"Created: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    books = [
        ("01_The_Little_Cloud_Who_Wanted_to_Rain", "The_Little_Cloud_Who_Wanted_to_Rain"),
        ("02_Luna_and_the_Moonlight_Garden", "Luna_and_the_Moonlight_Garden"),
        ("03_The_Robot_Who_Wanted_to_Dance", "The_Robot_Who_Wanted_to_Dance"),
    ]
    
    for book_dir, title in books:
        full_path = os.path.join("/home/user/children_books", book_dir)
        create_book_pdf(full_path, title)
