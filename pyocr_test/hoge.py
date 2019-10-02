from PIL import Image
import sys
import pyocr
import pyocr.builders
import cv2

tools = pyocr.get_available_tools()  # OCRツールの有無の確認
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print(tool.get_name())
langs = tool.get_available_languages()
print(langs)
lang = 'jpn'
print(lang)

txt = tool.image_to_string(
    Image.open('img/sample2.jpeg'),
    lang=lang,
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)
