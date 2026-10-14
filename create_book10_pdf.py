#!/usr/bin/env python3
"""
Create PDF for Book 10: The Little Library of Lost Things
Combines illustrations with text from manuscript
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

# Page size - using A4 (common for children's books)
PAGE_WIDTH, PAGE_HEIGHT = A4

# Colors for text
TITLE_COLOR = HexColor("#4a3728")  # Warm brown
TEXT_COLOR = HexColor("#3a2e28")  # Dark brown
COPYRIGHT_COLOR = HexColor("#6b5b47")  # Medium brown

# Fonts - using built-in fonts
TITLE_FONT = "Helvetica-Bold"
TEXT_FONT = "Helvetica"

# Read the manuscript to extract text for each page
page_texts = {}
current_page = None

with open(MANUSCRIPT_PATH, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line.startswith("PAGE "):
            # Extract page number
            parts = line.split(':')
            if len(parts) > 1:
                page_num = parts[0].replace("PAGE ", "").replace("-", "_")
                current_page = page_num
                page_texts[current_page] = ""
        elif line.startswith("[Illustration:") or line.startswith("==="):
            # Skip illustration notes and separators
            continue
        elif current_page and line:
            # Add text to current page
            if page_texts[current_page]:
                page_texts[current_page] += "\n"
            page_texts[current_page] += line

# Create PDF
c = canvas.Canvas(PDF_PATH, pagesize=A4)

# Page 1: Cover
if os.path.exists(COVER_PATH):
    cover_img = ImageReader(COVER_PATH)
    c.drawImage(cover_img, 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT, preserveAspectRatio=True, mask='auto')
else:
    # Fallback: create simple cover
    c.setFillColor(TITLE_COLOR)
    c.setFont(TITLE_FONT, 24)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2, TITLE)
    c.setFont(TEXT_FONT, 16)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 - 30, f"by {AUTHOR}")
c.showPage()

# Page 2-3: Title page
if os.path.exists(os.path.join(ILLUS_DIR, "page_02_03_title.png")):
    title_img = ImageReader(os.path.join(ILLUS_DIR, "page_02_03_title.png"))
    c.drawImage(title_img, 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT, preserveAspectRatio=True, mask='auto')
    
    # Add title text
    c.setFillColor(TITLE_COLOR)
    c.setFont(TITLE_FONT, 28)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 100, TITLE)
    c.setFont(TEXT_FONT, 18)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 140, f"Written by")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT - 165, AUTHOR)
c.showPage()

# Page 4: Copyright
if os.path.exists(os.path.join(ILLUS_DIR, "page_04_copyright.png")):
    copyright_img = ImageReader(os.path.join(ILLUS_DIR, "page_04_copyright.png"))
    c.drawImage(copyright_img, 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT, preserveAspectRatio=True, mask='auto')
    
    # Add copyright text
    c.setFillColor(COPYRIGHT_COLOR)
    c.setFont(TEXT_FONT, 12)
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2, f"Copyright © {YEAR} {AUTHOR}")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 - 20, "All rights reserved.")
    c.drawCentredString(PAGE_WIDTH/2, PAGE_HEIGHT/2 - 40, "Buyer has usage rights only.")
c.showPage()

# Pages 5-32: Story pages
# Map page numbers to illustration files
page_illustrations = {
    "5": "page_05.png",
    "6_7": "page_06_07.png",
    "8_9": "page_08_09.png",
    "10_11": "page_10_11.png",
    "12_13": "page_12_13.png",
    "14_15": "page_14_15.png",
    "16_17": "page_16_17.png",
    "18_19": "page_18_19.png",
    "20_21": "page_20_21.png",
    "22_23": "page_22_23.png",
    "24_25": "page_24_25.png",
    "26_27": "page_26_27.png",
    "28_29": "page_28_29.png",
    "30_31": "page_30_31.png",
    "32": "page_32.png",
}

# Add story pages
for page_num, illus_file in page_illustrations.items():
    illus_path = os.path.join(ILLUS_DIR, illus_file)
    
    if os.path.exists(illus_path):
        img = ImageReader(illus_path)
        c.drawImage(img, 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT, preserveAspectRatio=True, mask='auto')
    
    # Add text for this page if it exists
    if page_num in page_texts:
        text = page_texts[page_num]
        if text:
            # Split text into lines
            lines = text.split('\n')
            c.setFillColor(TEXT_COLOR)
            c.setFont(TEXT_FONT, 14)
            
            # Position text at top with some margin
            y_position = PAGE_HEIGHT - 50
            for line in lines:
                if line.strip():  # Only draw non-empty lines
                    c.drawCentredString(PAGE_WIDTH/2, y_position, line.strip())
                    y_position -= 20
    
    c.showPage()

# Save PDF
c.save()

print(f"✅ PDF created successfully at: {PDF_PATH}")
print(f"   Total pages: {c.getPageNumber()}")
