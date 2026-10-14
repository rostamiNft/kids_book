#!/usr/bin/env python3
"""
Generate proper, sellable PDFs for children's books
Combines text and illustrations into professional PDFs
"""

from fpdf import FPDF
import os

# Constants
INCH = 25.4  # mm per inch
BOOK_WIDTH_MM = 8 * INCH  # 8 inches
BOOK_HEIGHT_MM = 10 * INCH  # 10 inches
MARGIN_MM = 12.7  # 0.5 inches

# Book configurations
BOOKS = {
    "04_The_Day_the_Colors_Ran_Away": {
        "title": "The Day the Colors Ran Away",
        "author": "Hamidreza Rostami",
        "pages": 32,
        "page_order": [
            ("cover/front_cover.png", "cover", None),
            ("illustrations/page_02_03_title.png", "title", "The Day the Colors Ran Away\n\nWritten by\nHamidreza Rostami"),
            ("illustrations/page_04_copyright.png", "text", "The Day the Colors Ran Away\n\nWritten by Hamidreza Rostami\n\nCopyright (c) 2026 Hamidreza Rostami\nAll rights reserved.\nBuyer has usage rights only."),
            ("illustrations/page_01.png", "story", None),
            ("illustrations/page_05.png", "story", "Milo loved colors.\n\nHe loved the red of strawberries, the blue of the sky, the green of the grass, and especially the yellow of his favorite crayon.\n\nOne morning, Milo woke up and something was... wrong."),
            ("illustrations/page_06_07.png", "story", "The world was gray.\n\nNot just a little gray. Completely, totally, absolutely gray.\n\nThe sky was gray. The trees were gray. Even Milo's red pajamas were... gray."),
            ("illustrations/page_08.png", "story", None),
            ("illustrations/page_09.png", "story", None),
            ("illustrations/page_10_11.png", "story", "Milo ran downstairs. 'Mom! Dad! The colors are gone!'\n\nHis parents looked up from their gray breakfast. 'What do you mean, honey?' Mom asked.\n\nMilo held up his crayon box. All the crayons were gray. 'The colors ran away!'"),
            ("illustrations/page_12_13.png", "story", None),
            ("illustrations/page_14_15.png", "story", None),
            ("illustrations/page_16_17.png", "story", None),
            ("illustrations/page_18_19.png", "story", None),
            ("illustrations/page_20_21.png", "story", None),
            ("illustrations/page_22_23.png", "story", None),
            ("illustrations/page_24_25.png", "story", None),
            ("illustrations/page_26_27.png", "story", None),
            ("illustrations/page_28_29.png", "story", None),
            ("illustrations/page_30_31.png", "story", None),
            ("illustrations/page_32.png", "story", None),
        ]
    },
    "05_Captain_Whiskers_and_the_Great_Yarn_Adventure": {
        "title": "Captain Whiskers and the Great Yarn Adventure",
        "author": "Hamidreza Rostami",
        "pages": 30,
        "page_order": [
            ("cover/front_cover.png", "cover", None),
            ("illustrations/page_02_03_title.png", "title", "Captain Whiskers and the Great Yarn Adventure\n\nWritten by\nHamidreza Rostami"),
            ("illustrations/page_04_copyright.png", "text", "Captain Whiskers and the Great Yarn Adventure\n\nWritten by Hamidreza Rostami\n\nCopyright (c) 2026 Hamidreza Rostami\nAll rights reserved.\nBuyer has usage rights only."),
            ("illustrations/page_01.png", "story", None),
            ("illustrations/page_05.png", "story", None),
            ("illustrations/page_06_07.png", "story", None),
            ("illustrations/page_08_09.png", "story", None),
            ("illustrations/page_10_11.png", "story", None),
            ("illustrations/page_12_13.png", "story", None),
            ("illustrations/page_14_15.png", "story", None),
            ("illustrations/page_16.png", "story", None),
            ("illustrations/page_18.png", "story", None),
            ("illustrations/page_20.png", "story", None),
            ("illustrations/page_22.png", "story", None),
            ("illustrations/page_24.png", "story", None),
            ("illustrations/page_26.png", "story", None),
            ("illustrations/page_28.png", "story", None),
            ("illustrations/page_30.png", "story", None),
        ]
    },
    "06_The_Tiny_Giant": {
        "title": "The Tiny Giant",
        "author": "Hamidreza Rostami",
        "pages": 28,
        "page_order": [
            ("cover/front_cover.png", "cover", None),
            ("illustrations/page_02_03_title.png", "title", "The Tiny Giant\n\nWritten by\nHamidreza Rostami"),
            ("illustrations/page_04_copyright.png", "text", "The Tiny Giant\n\nWritten by Hamidreza Rostami\n\nCopyright (c) 2026 Hamidreza Rostami\nAll rights reserved.\nBuyer has usage rights only."),
            ("illustrations/page_01.png", "story", None),
            ("illustrations/page_05.png", "story", None),
            ("illustrations/page_06_07.png", "story", None),
            ("illustrations/page_08_09.png", "story", None),
            ("illustrations/page_10_11.png", "story", None),
            ("illustrations/page_12_13.png", "story", None),
            ("illustrations/page_14_15.png", "story", None),
            ("illustrations/page_16_17.png", "story", None),
            ("illustrations/page_18_19.png", "story", None),
            ("illustrations/page_20_21.png", "story", None),
            ("illustrations/page_22_23.png", "story", None),
            ("illustrations/page_24_25.png", "story", None),
            ("illustrations/page_26_27.png", "story", None),
            ("illustrations/page_28.png", "story", None),
        ]
    },
    "07_The_Quiet_Little_Drum": {
        "title": "The Quiet Little Drum",
        "author": "Hamidreza Rostami", 
        "pages": 26,
        "page_order": []
    },
    "08_The_Last_Leaf_of_Autumn": {
        "title": "The Last Leaf of Autumn",
        "author": "Hamidreza Rostami",
        "pages": 28,
        "page_order": []
    },
    "09_The_Boy_Who_Painted_Dreams": {
        "title": "The Boy Who Painted Dreams",
        "author": "Hamidreza Rostami",
        "pages": 30,
        "page_order": []
    },
    "10_The_Little_Library_of_Lost_Things": {
        "title": "The Little Library of Lost Things",
        "author": "Hamidreza Rostami",
        "pages": 32,
        "page_order": []
    }
}

def create_pdf(book_key, book_config):
    """Create a proper PDF for a book"""
    base_dir = f"/home/user/children_books/{book_key}"
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    
    pdf = FPDF(unit="mm", format=(BOOK_WIDTH_MM, BOOK_HEIGHT_MM))
    pdf.set_auto_page_break(False)
    
    for img_file, page_type, text in book_config["page_order"]:
        img_path = os.path.join(base_dir, img_file)
        
        if not os.path.exists(img_path):
            print(f"  Warning: Missing {img_path}")
            continue
        
        pdf.add_page()
        
        # Add image
        pdf.image(img_path, 0, 0, BOOK_WIDTH_MM, BOOK_HEIGHT_MM)
        
        # Add text if needed
        if text:
            pdf.set_font("Helvetica", "", 12)
            pdf.set_text_color(0, 0, 0)
            # Split text by newlines and add line by line
            lines = text.split('\n')
            y = MARGIN_MM
            for line in lines:
                if line.strip():
                    pdf.set_xy(MARGIN_MM, y)
                    pdf.cell(0, 10, line, ln=True, align='C')
                    y += 8
    
    pdf_path = os.path.join(pdf_dir, f"{book_config['title'].replace(' ', '_')}.pdf")
    pdf.output(pdf_path)
    print(f"  Created: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    print("Creating proper PDFs...")
    print("=" * 60)
    
    for key, config in BOOKS.items():
        if config["page_order"]:  # Only process books with page_order defined
            print(f"\nProcessing: {config['title']}")
            create_pdf(key, config)
    
    print("\n" + "=" * 60)
    print("PDF generation complete!")
