import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pptx import Presentation
from pptx.util import Inches, Pt, Centipoints
from pptx.enum.text import PP_ALIGN, MSO_AUTO_SIZE
import config
import pptx
# ContentObject := Text | Image | ...
# Assume that objectList is sorted by page & coordinates

from assembler.header import addHeader
# Version 1
def assemble(contentObjectList, outputFileName): # [] ContentObject
    prs = Presentation()
    titleSlideLayout = prs.slide_layouts[6] # blank
    currentPage = -1
    width = prs.slide_width
    height = prs.slide_height
    slideShape = None
    tf = None
    for contentObject in contentObjectList:
        if (currentPage != contentObject["pageNumber"]): #update page number
            slide = prs.slides.add_slide(titleSlideLayout)
            slideShape = slide.shapes 
            addHeader(slideShape, width, height / 10)
            currentPage += 1
            txBox = slideShape.add_textbox(width / 10, height / 6, 4 * width / 5, 0)
            tf = txBox.text_frame
            tf.word_wrap  = True
            
            
        if contentObject["contentType"] == "text":
            p = tf.add_paragraph()

            p.level = 0
            p.text = contentObject["content"]
            p.font.name = config.FONT_FAMILY
            p.font.size = Pt(config.PARAGRAPH_FONT_SIZE)
            p.space_after = Pt(config.PARAGRAPH_FONT_SIZE)
            

        if contentObject["contentType"] == "image":
            slideShape.add_picture(contentObject["imagePath"], width / 2, 3 * height / 5, width / 4)

    prs.save(outputFileName)