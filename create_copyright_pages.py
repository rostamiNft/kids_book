#!/usr/bin/env python3
"""
Create copyright pages with proper text
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Constants
WIDTH = 8 * 300  # 8 inches at 300 DPI
HEIGHT = 10 * 300  # 10 inches at 300 DPI

# Try to find a font
font_paths = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    "/usr/share/fonts/TTF/DejaVuSerif.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSerif.ttf",
]

font = None
for path in font_paths:
    try:
        font = ImageFont.truetype(path, 36)
        break
    except:
        pass

if font is None:
    font = ImageFont.load_default()
    print("Using default font")

books = [
    ("01_The_Little_Cloud_Who_Wanted_to_Rain", "The Little Cloud Who Wanted to Rain"),
    ("02_Luna_and_the_Moonlight_Garden", "Luna and the Moonlight Garden"),
    ("03_The_Robot_Who_Wanted_to_Dance", "The Robot Who Wanted to Dance"),
]

for book_dir, title in books:
    ill_dir = f"/home/user/children_books/{book_dir}/illustrations"
    
    # Create copyright page
    img = Image.new('RGB', (WIDTH, HEIGHT), color='white')
    draw = ImageDraw.Draw(img)
    
    # Add some decorative elements
    # Draw a simple border
    draw.rectangle([(50, 50), (WIDTH-50, HEIGHT-50)], outline=(200, 200, 200), width=2)
    
    # Add text
    y = HEIGHT // 2 - 100
    
    # Title
    draw.text((WIDTH/2, y), title, fill=(0, 0, 0), font=font, anchor='mt')
    y += 50
    
    # Author
    draw.text((WIDTH/2, y), "Written by Hamidreza Rostami", fill=(100, 100, 100), font=font, anchor='mt')
    y += 60
    
    # Copyright
    draw.text((WIDTH/2, y), "Copyright (c) 2026 Hamidreza Rostami", fill=(0, 0, 0), font=font, anchor='mt')
    y += 40
    
    draw.text((WIDTH/2, y), "All rights reserved.", fill=(0, 0, 0), font=font, anchor='mt')
    y += 40
    
    draw.text((WIDTH/2, y), "Buyer has usage rights only.", fill=(0, 0, 0), font=font, anchor='mt')
    
    # Save
    output_path = os.path.join(ill_dir, "page_04_copyright.png")
    img.save(output_path)
    print(f"Created: {output_path}")

print("\nAll copyright pages created!")
