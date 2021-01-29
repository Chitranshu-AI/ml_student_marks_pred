# Import libraries
import pandas as pd
import pytesseract as pt
import pdf2image
# Read a pdf file as image pages


# pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
pt.pytesseract.tesseract_cmd = 'C:\Program Files\\tesseract\\tesseract.exe'
images = pdf2image.convert_from_path("5019.pdf", 500,poppler_path='C:\Program Files\poppler-0.68.0\\bin')


# Save all pages as images
for i in range(len(images)):
    images[i].save('images\\image_' + str(i) + '.jpg')
# Convert a page to a string (page 2)
# content = pt.image_to_string(images[0], lang='swe')
text = pt.image_to_string(images[0], lang = 'eng')

# print(text)





