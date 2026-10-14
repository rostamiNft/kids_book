#!/usr/bin/env python3
"""
Create PDF for Book 10: The Little Library of Lost Things
Properly handles 32 pages with spreads
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import os

# Book metadata
TITLE = "The Little Library of Lost Things"
AUTHOR = "Hamidreza Rostami"
YEAR = "2026"

# Paths
BOOK_DIR = "/home/user/children_books/10_The_Little_Library_of_Lost_Things"
COVER_PATH = os.path.join(BOOK_DIR, "cover", "front_cover.png")
ILLUS_DIR = os.path.join(BOOK_DIR, "illustrations")
MANUSCRIPT_PATH = os.path.join(BOOK_DIR, "manuscript", "story.txt")
PDF_PATH = os.path.join(BOOK_DIR, "pdf", "The_Little_Library_of_Lost_Things.pdf")

# Page size
PAGE_WIDTH, PAGE_HEIGHT = A4

# Colors
TITLE_COLOR = HexColor("#4a3728")
TEXT_COLOR = HexColor("#3a2e28")
COPYRIGHT_COLOR = HexColor("#6b5b47")

# Fonts
TITLE_FONT = "Helvetica-Bold"
TEXT_FONT = "Helvetica"

# Read manuscript
page_texts = {}
current_page = None

with open(MANUSCRIPT_PATH, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith("PAGE "):
            parts = line.split(':')
            if len(parts) > 1:
                page_num = parts[0].replace("PAGE ", "").replace("-", "_")
                current_page = page_num
                page_texts[current_page] = ""
        elif line.startswith("[Illustration:") or line.startswith("==="):
            continue
        elif current_page and line:
            if page_texts[current_page]:
                page_texts[current_page] += "\n"
            page_texts[current_page] += line

# Page layout configuration
# Each entry: (page_number(s), illustration_file, text_key)
pages_config = [
    # Page 1: Cover
    {"pages": [1], "illus": "front_cover.png", "illus_dir": "cover", "text": None},
    
    # Pages 2-3: Title spread
    {"pages": [2, 3], "illus": "page_02_03_title.png", "text": "2_3"},
    
    # Page 4: Copyright
    {"pages": [4], "illus": "page_04_copyright.png", "text": "4"},
    
    # Page 5: Single page
    {"pages": [5], "illus": "page_05.png", "text": "5"},
    
    # Pages 6-7: Spread
    {"pages": [6, 7], "illus": "page_06_07.png", "text": "6_7"},
    
    # Pages 8-9: Spread
    {"pages": [8, 9], "illus": "page_08_09.png", "text": "8_9"},
    
    # Pages 10-11: Spread
    {"pages": [10, 11], "illus": "page_10_11.png", "text": "10_11"},
    
    # Pages 12-13: Spread
    {"pages": [12, 13], "illus": "page_12_13.png", "text": "12_13"},
    
    # Pages 14-15: Spread
    {"pages": [14, 15], "illus": "page_14_15.png", "text": "14_15"},
    
    # Pages 16-17: Spread
    {"pages": [16, 17], "illus": "page_16_17.png", "text": "16_17"},
    
    # Pages 18-19: Spread
    {"pages": [18, 19], "illus": "page_18_19.png", "text": "18_19"},
    
    # Pages 20-21: Spread
    {"pages": [20, 21], "illus": "page_20_21.png", "text": "20_21"},
    
    # Pages 22-23: Spread
    {"pages": [22, 23], "illus": "page_22_23.png", "text": "22_23"},
    
    # Pages 24-25: Spread
    {"pages": [24, 25], "illus": "page_24_25.png", "text": "24_25"},
    
    # Pages 26-27: Spread
    {"pages": [26, 27], "illus": "page_26_27.png", "text": "26_27"},
    
    # Pages 28-29: Spread
    {"pages": [28, 29], "illus": "page_28_29.png", "text": "28_29"},
    
    # Pages 30-31: Spread
    {"pages": [30, 31], "illus": "page_30_31.png", "text": "30_31"},
    
    # Page 32: Final page
    {"pages": [32], "illus": "page_32.png", "text": "32"},
]

# Create PDF
c = canvas.Canvas(PDF_PATH, pagesize=A4)

for config in pages_config:
    pages = config["pages"]
    illus = config["illus"]
    text_key = config.get("text")
    illus_dir = config.get("illus_dir", "illustrations")
    
    illus_path = os.path.join(BOOK_DIR, illus_dir, illus)
    
    for page_num in pages:
        # Draw illustration
        if os.path.exists(illus_path):
            img = ImageReader(illus_path)
            img_width, img_height = img.getSize()
            aspect = img_height / float(img_width)
            
            # Calculate dimensions to fit page
            if aspect > (PAGE_HEIGHT / PAGE_WIDTH):
                # Image is taller than page proportion
                draw_height = PAGE_HEIGHT
                draw_width = draw_height / aspect
            else:
                # Image is wider than page proportion
                draw_width = PAGE_WIDTH
                draw_height = draw_width * aspect
            
            # Center the image
            x_offset = (PAGE_WIDTH - draw_width) / 2
            y_offset = (PAGE_HEIGHT - draw_height) / 2
            
            c.drawImage(img, x_offset, y_offset, width=draw_width, height=draw_height, mask='auto')
        
        # Add text if this is the first page of the spread
        if page_num == pages[0] and text_key and text_key in page_texts:
            text = page_texts[text_key]
            if text:
                lines = [l.strip() for l in text.split('\n') if l.strip()]
                c.setFillColor(TEXT_COLOR)
                c.setFont(TEXT_FONT, 14)
                
                y_position = PAGE_HEIGHT - 50
                for line in lines:
                    c.drawCentredString(PAGE_WIDTH/2, y_position, line)
                    y_position -= 20
        
        # Add title on title page
        if page_num == 2:
            c.setFillColor(TITLE_COLOR)
            c.setFont(TITLE_FONT, 28)
            c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 100, TITLE)
            c.setFont(TEXT_FONT, 18)
            c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 140, "Written by")
            c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 165, AUTHOR)
        
        # Add copyright text on copyright page
        if page_num == 4:
            c.setFillColor(COPYRIGHT_COLOR)
            c.setFont(TEXT_FONT, 12)
            c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2, f"Copyright © {YEAR} {AUTHOR}")
            c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 - 20, "All rights reserved.")
            c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 - 40, "Buyer has usage rights only.")
        
        c.showPage()

# Save PDF
c.save()

print(f"✅ PDF created successfully at: {PDF_PATH}")
print(f"   Total pages: {c.getPageNumber()}")
