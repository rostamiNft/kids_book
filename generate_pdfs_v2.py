#!/usr/bin/env python3
"""
Generate PDFs for children's books - Version 2
Creates PDFs by combining images in order
"""

import img2pdf
import os

# Book configurations
BOOKS = [
    {
        "dir": "01_The_Little_Cloud_Who_Wanted_to_Rain",
        "title": "The Little Cloud Who Wanted to Rain",
        "page_order": [
            "cover/front_cover.png",
            "illustrations/page_02_03_title.png",
            "illustrations/page_04_copyright.png",
            "illustrations/page_01.png",
            "illustrations/page_05.png",
            "illustrations/page_06_07.png",
            "illustrations/page_08_09.png",
            "illustrations/page_10_11.png",
            "illustrations/page_12_13.png",
            "illustrations/page_14_15.png",
            "illustrations/page_16_17.png",
            "illustrations/page_18_19.png",
            "illustrations/page_20_21.png",
            "illustrations/page_22_23.png",
            "illustrations/page_24_25.png",
            "illustrations/page_26_27.png",
            "illustrations/page_28.png",
        ]
    },
    {
        "dir": "02_Luna_and_the_Moonlight_Garden",
        "title": "Luna and the Moonlight Garden",
        "page_order": [
            "cover/front_cover.png",
            "illustrations/page_02_03_title.png",
            "illustrations/page_04_copyright.png",
            "illustrations/page_01.png",
            "illustrations/page_05.png",
            "illustrations/page_06_07.png",
            "illustrations/page_08_09.png",
            "illustrations/page_09.png",
            "illustrations/page_10_11.png",
            "illustrations/page_12_13.png",
            "illustrations/page_14_15.png",
            "illustrations/page_16_17.png",
            "illustrations/page_18_19.png",
            "illustrations/page_20_21.png",
            "illustrations/page_22_23.png",
            "illustrations/page_24_25.png",
            "illustrations/page_26_27.png",
            "illustrations/page_28_29.png",
            "illustrations/page_30.png",
        ]
    },
    {
        "dir": "03_The_Robot_Who_Wanted_to_Dance",
        "title": "The Robot Who Wanted to Dance",
        "page_order": [
            "cover/front_cover.png",
            "illustrations/page_02_03_title.png",
            "illustrations/page_04_copyright.png",
            "illustrations/page_01.png",
            "illustrations/page_05.png",
            "illustrations/page_06_07.png",
            "illustrations/page_08_09.png",
            "illustrations/page_09.png",
            "illustrations/page_10_11.png",
            "illustrations/page_12.png",
            "illustrations/page_13.png",
            "illustrations/page_14_15.png",
            "illustrations/page_16_17.png",
            "illustrations/page_18_19.png",
            "illustrations/page_20_21.png",
            "illustrations/page_22_23.png",
            "illustrations/page_24_25.png",
            "illustrations/page_26_27.png",
            "illustrations/page_28.png",
        ]
    }
]


def create_pdf(book_config):
    """Create PDF for a single book"""
    base_dir = f"/home/user/children_books/{book_config['dir']}"
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    
    # Collect all image paths
    image_paths = []
    for page in book_config["page_order"]:
        full_path = os.path.join(base_dir, page)
        if os.path.exists(full_path):
            image_paths.append(full_path)
        else:
            print(f"Warning: Missing file {full_path}")
    
    # Create PDF
    pdf_path = os.path.join(pdf_dir, f"{book_config['title'].replace(' ', '_')}.pdf")
    
    try:
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(image_paths))
        print(f"✓ Created: {pdf_path}")
        return pdf_path
    except Exception as e:
        print(f"✗ Error creating {pdf_path}: {e}")
        return None


if __name__ == "__main__":
    print("Creating PDFs for children's books...")
    print("=" * 60)
    
    for book in BOOKS:
        create_pdf(book)
    
    print("=" * 60)
    print("PDF generation complete!")
