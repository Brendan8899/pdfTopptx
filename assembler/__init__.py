import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pptx import Presentation
<<<<<<< HEAD
from pptx.util import Inches
=======
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_AUTO_SIZE
import config
>>>>>>> 841f17ee5c70221d91489df5f55f65b3c924309b
# ContentObject := Text | Image | ...
# Assume that objectList is sorted by page & coordinates

from assembler.utils import makeParaBulletPointed
from assembler.header import addHeader
# Version 1
def assemble(contentObjectList, outputFileName): # [] ContentObject
    contentObjectList.sort(key = lambda a: a["pageNumber"])
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
            txBox = slideShape.add_textbox(width / 12, height / 8, 4 * width / 5, height)
            tf = txBox.text_frame
            tf.word_wrap  = True
            
        if contentObject["contentType"] == "text":
            p = tf.add_paragraph()
            makeParaBulletPointed(p)
            
            p.add_run()
            p.level = 0
            p.text = contentObject["content"]
            p.font.name = config.FONT_FAMILY
            p.font.size = pptx.util.Pt(config.PARAGRAPH_FONT_SIZE)

        if contentObject["contentType"] == "image":
<<<<<<< HEAD
            slideShape.add_picture(contentObject["imagePath"], Inches(0.5), Inches(1.75))
        if contentObject["contentType"] == "table":
            rows, columns = contentObject["dataFrame"].shape
            print("Reaches here")
            print(contentObject["dataFrame"].shape)
            x, y, cx, cy = Inches(2), Inches(2), Inches(4), Inches(1.5)
            # Add table to the slide
            graphic_frame = slide.shapes.add_table(rows, columns, x, y, cx, cy)
            table = graphic_frame.table

            # Populate the table with DataFrame values
            for i in range(rows):
                for j in range(columns):
                    cell = table.cell(i, j)
                    cell.text = str(contentObject["dataFrame"].iat[i, j])
=======
            slideShape.add_picture(contentObject["imagePath"], width/4, height / 2, width / 2)

>>>>>>> 841f17ee5c70221d91489df5f55f65b3c924309b
    prs.save(outputFileName)