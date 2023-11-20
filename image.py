import pdfplumber
from PIL import Image
#import os

def save_pdf_page_as_png(pdf_path, page_number, output_path):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number - 1]
        image = page.to_image(resolution = 150)  
		# Adjust the resolution as needed, this seems to be best resolution.
		# available formats: tiff, bmp, png, 
        image.save(output_path, format='png')

# Example usage
pdf_path = "MSRP-C3_14.pdf"
page_number = 264  # Specify the page number you want to save (starting from 1)
output_path = '264.png'

save_pdf_page_as_png(pdf_path, page_number, output_path)

#--file_size = os.path.getsize(output_path)
#--print(f"PNG file size: {file_size} bytes")
