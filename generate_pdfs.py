#!/usr/bin/env python3
"""
Generate PDFs for children's books
Creates text pages as images and combines with illustrations into PDFs
"""

from PIL import Image, ImageDraw, ImageFont
import img2pdf
import os

# Constants
BOOK_WIDTH = 8 * 300  # 8 inches at 300 DPI
BOOK_HEIGHT = 10 * 300  # 10 inches at 300 DPI
MARGIN = 0.5 * 300  # 0.5 inches at 300 DPI
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"


def create_text_page(text, page_num, output_dir, font_size=24, is_title=False, is_copyright=False):
    """Create a text-only page as an image"""
    img = Image.new('RGB', (BOOK_WIDTH, BOOK_HEIGHT), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        if is_title:
            font = ImageFont.truetype(FONT_PATH, font_size * 2)
        else:
            font = ImageFont.truetype(FONT_PATH, font_size)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position
    x = MARGIN
    y = MARGIN
    
    if is_title:
        # Center the title
        draw.text((BOOK_WIDTH/2, BOOK_HEIGHT/2 - 100), text, fill='black', font=font, anchor='mt')
    elif is_copyright:
        # Center the copyright text
        lines = text.split('\n')
        for i, line in enumerate(lines):
            draw.text((BOOK_WIDTH/2, BOOK_HEIGHT/2 - 50 + i * 40), line, fill='black', font=font, anchor='mt')
    else:
        # Story text - wrap if needed
        lines = text.split('\n')
        for i, line in enumerate(lines):
            draw.text((MARGIN, MARGIN + i * 40), line, fill='black', font=font)
    
    output_path = os.path.join(output_dir, f"page_{page_num:02d}_text.png")
    img.save(output_path)
    return output_path


def create_book_pdf(book_dir, book_title, author="Hamidreza Rostami"):
    """Create PDF for a book"""
    illustrations_dir = os.path.join(book_dir, "illustrations")
    cover_dir = os.path.join(book_dir, "cover")
    pdf_dir = os.path.join(book_dir, "pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Collect all pages in order
    pages = []
    
    # 1. Cover
    cover_path = os.path.join(cover_dir, "front_cover.png")
    if os.path.exists(cover_path):
        pages.append(cover_path)
    
    # 2. Title page (page 2-3)
    title_img_path = os.path.join(illustrations_dir, "page_02_03_title.png")
    if os.path.exists(title_img_path):
        pages.append(title_img_path)
    else:
        # Create title page
        title_text = f"{book_title}\n\nWritten by\n{author}"
        pages.append(create_text_page(title_text, 2, illustrations_dir, is_title=True))
    
    # 3. Copyright page (page 4)
    copyright_text = f"{book_title}\n\nWritten by {author}\n\nCopyright (c) 2026 Hamidreza Rostami\nAll rights reserved.\nBuyer has usage rights only."
    copyright_path = os.path.join(illustrations_dir, "page_04_copyright.png")
    if os.path.exists(copyright_path):
        pages.append(copyright_path)
    else:
        pages.append(create_text_page(copyright_text, 4, illustrations_dir, is_copyright=True))
    
    # 4. Story pages
    # Get all illustration files and sort them
    ill_files = [f for f in os.listdir(illustrations_dir) if f.endswith('.png') and f != 'page_02_03_title.png' and f != 'page_04_copyright.png']
    ill_files.sort()
    
    for f in ill_files:
        pages.append(os.path.join(illustrations_dir, f))
    
    # Create PDF
    pdf_path = os.path.join(pdf_dir, f"{book_title.replace(' ', '_')}.pdf")
    
    # Convert to PDF
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert(pages))
    
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
    
    print("\nAll PDFs created successfully!")
