import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from interpreter.text import isText
import pptx
from pptx import Presentation
import config
# ContentObject := Text | Image | ...
# Assume that objectList is sorted by page & coordinates

# Version 1
def assemble(contentObjectList, outputFileName): # [] ContentObject
    prs = Presentation()
    titleSlideLayout = prs.slide_layouts[6] # Blank
    currentPage = -1
    width = prs.slide_width
    height = prs.slide_height
    slideShape = None
    tf = None
    for contentObject in contentObjectList:
        if (currentPage != contentObject["pageNumber"]): #update page number
            slide = prs.slides.add_slide(titleSlideLayout)
            slideShape = slide.shapes 
            txBox = slideShape.add_textbox(0, 0, width / 2, height / 2 )
            tf = txBox.text_frame
            tf.word_wrap = True
            currentPage += 1
        
        if contentObject["contentType"] == "text":
            p = tf.add_paragraph()
            p.text = contentObject["content"]
            p.font.size = pptx.util.Pt(config.PARAGRAPH_FONT_SIZE)

        if contentObject["contentType"] == "image":
            slideShape.add_picture(contentObject["imagePath"], width / 2, height / 6, width / 2)

    prs.save(outputFileName)