#!/usr/bin/env python3
"""
Create final, sellable PDFs using WeasyPrint
Properly combines text and illustrations
"""

from weasyprint import HTML
import os

# Book configurations with page text
BOOKS = {
    "04": {
        "dir": "04_The_Day_the_Colors_Ran_Away",
        "title": "The Day the Colors Ran Away",
        "author": "Hamidreza Rostami",
        "pages": {
            "cover": {"img": "cover/front_cover.png", "text": None},
            "02_03": {"img": "illustrations/page_02_03_title.png", "text": "The Day the Colors Ran Away<br><br>Written by<br>Hamidreza Rostami"},
            "04": {"img": None, "text": "The Day the Colors Ran Away<br><br>Written by Hamidreza Rostami<br><br>Copyright (c) 2026 Hamidreza Rostami<br>All rights reserved.<br>Buyer has usage rights only."},
            "01": {"img": "illustrations/page_01.png", "text": None},
            "05": {"img": "illustrations/page_05.png", "text": "Milo loved colors.<br><br>He loved the red of strawberries, the blue of the sky, the green of the grass, and especially the yellow of his favorite crayon.<br><br>One morning, Milo woke up and something was... wrong."},
            "06_07": {"img": "illustrations/page_06_07.png", "text": "The world was gray.<br><br>Not just a little gray. Completely, totally, absolutely gray.<br><br>The sky was gray. The trees were gray. Even Milo's red pajamas were... gray.<br><br>\"That's strange,\" Milo said, poking his pajamas. \"They were red yesterday.\""},
            "08": {"img": "illustrations/page_08.png", "text": "Milo ran downstairs. \"Mom! Dad! The colors are gone!\"<br><br>His parents looked up from their gray breakfast. \"What do you mean, honey?\" Mom asked.<br><br>Milo held up his crayon box. All the crayons were gray. \"The colors ran away!\""},
            "09": {"img": "illustrations/page_09.png", "text": "Milo's dad checked the TV. It was gray. Mom looked out the window. Gray.<br><br>\"This is odd,\" Dad said.<br><br>Milo grabbed his backpack. \"I'm going to find them!\""},
            "10_11": {"img": "illustrations/page_10_11.png", "text": "Milo stepped outside. The world looked like an old movie. No red stop signs. No green grass. No blue sky.<br><br>Just gray.<br><br>Then he heard it. A soft giggle."},
            "12_13": {"img": "illustrations/page_12_13.png", "text": "He followed the sound to the park. And there, sitting on a gray swing, was a small, round figure.<br><br>It was Red. The color red, in the shape of a little person with rosy cheeks and a bright red dress.<br><br>\"Hello, Milo,\" Red said, swinging her legs. \"Looking for us?\""},
            "14_15": {"img": "illustrations/page_14_15.png", "text": "\"Yes!\" Milo said. \"Where are all the colors? The world is so... boring without you!\"<br><br>Red giggled. \"We just wanted a day off. Being a color is hard work, you know.\"<br><br>\"But... but we need you!\" Milo said."},
            "16_17": {"img": "illustrations/page_16_17.png", "text": "Red hopped off the swing. \"Come on. I'll show you.\"<br><br>She took Milo's hand and led him to a clearing in the park. There, Milo saw them all.<br><br>Blue was napping under a tree. Green was reading a book. Yellow was eating a (gray) sandwich."},
            "18_19": {"img": "illustrations/page_18_19.png", "text": "\"Maybe... maybe you're not meant to be loud.\"<br><br>She held Drum close to her ear and whispered, \"Maybe you're meant to be quiet.\"<br><br>And then, Drum heard it.<br><br>The softest sound. Like a heartbeat. Like a secret.<br><br>It was his sound."},
            "20_21": {"img": "illustrations/page_20_21.png", "text": None},
            "22_23": {"img": "illustrations/page_22_23.png", "text": None},
            "24_25": {"img": "illustrations/page_24_25.png", "text": None},
            "26_27": {"img": "illustrations/page_26_27.png", "text": None},
            "28_29": {"img": "illustrations/page_28_29.png", "text": None},
            "30_31": {"img": "illustrations/page_30_31.png", "text": None},
            "32": {"img": "illustrations/page_32.png", "text": None},
        }
    }
}

def create_html(book_key, book_data):
    """Create HTML for a book"""
    base_dir = f"/home/user/children_books/{book_data['dir']}"
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  body {{ width: 8in; height: 10in; margin: 0; padding: 0; background: white; }}
  .page {{ width: 8in; height: 10in; position: relative; page-break-after: always; }}
  img {{ max-width: 8in; max-height: 10in; object-fit: contain; position: absolute; top: 0; left: 0; }}
  .text {{ position: absolute; bottom: 0.5in; left: 0.5in; right: 0.5in; font-family: Georgia, serif; font-size: 16pt; line-height: 1.5; text-align: center; color: #333; }}
  .title-text {{ font-size: 20pt; font-weight: bold; }}
  .copyright-text {{ font-size: 12pt; line-height: 1.6; }}
  .cover img {{ width: 8in; height: 10in; object-fit: cover; }}
</style>
</head>
<body>
'''
    
    for page_key, content in book_data['pages'].items():
        html += '<div class="page">'
        if content['img']:
            img_path = os.path.join(base_dir, content['img'])
            if 'cover' in page_key:
                html += f'<img src="{img_path}" class="cover">'
            else:
                html += f'<img src="{img_path}">'
        
        if content['text']:
            if 'copyright' in content['text'].lower() or 'Copyright' in content['text']:
                html += f'<div class="text copyright-text">{content["text"]}</div>'
            elif 'Written by' in content['text']:
                html += f'<div class="text title-text">{content["text"]}</div>'
            else:
                html += f'<div class="text">{content["text"]}</div>'
        
        html += '</div>\n'
    
    html += '</body></html>'
    return html


def create_pdf(book_key, book_data):
    """Create PDF from HTML"""
    base_dir = f"/home/user/children_books/{book_data['dir']}"
    pdf_dir = os.path.join(base_dir, "pdf")
    os.makedirs(pdf_dir, exist_ok=True)
    
    html = create_html(book_key, book_data)
    
    # Save HTML temporarily
    html_path = os.path.join(base_dir, "temp.html")
    with open(html_path, 'w') as f:
        f.write(html)
    
    # Convert to PDF
    pdf_path = os.path.join(pdf_dir, f"{book_data['title'].replace(' ', '_')}.pdf")
    HTML(html_path, base_url=base_dir).write_pdf(pdf_path)
    
    # Clean up
    os.remove(html_path)
    
    print(f"  Created: {pdf_path}")
    return pdf_path


if __name__ == "__main__":
    print("Creating final sellable PDFs...")
    print("=" * 60)
    
    for key, data in BOOKS.items():
        print(f"\nProcessing: {data['title']}")
        create_pdf(key, data)
    
    print("\n" + "=" * 60)
    print("PDF generation complete!")
