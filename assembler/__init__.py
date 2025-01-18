import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from interpreter.text import isText
import pptx
from pptx import Presentation
# ContentObject := Text | Image | ...
# Assume that objectList is sorted by page & coordinates

# Version 1
def assemble(contentObjectList, outputFileName): # [] ContentObject
    prs = Presentation()
    titleSlideLayout = prs.slide_layouts[1] 
    currentPage = -1
    
    slideShape = None
    for contentObject in contentObjectList:
        if (currentPage != contentObject["pageNumber"]): #update page number
            slide = prs.slides.add_slide(titleSlideLayout)
            slideShape = slide.shapes 
            currentPage += 1
            
        titleShape = slideShape.title
        bodyShape = slideShape.placeholders[1]
        titleShape.text = "[TITLE]"
        if contentObject["contentType"] == "text":
            bodyShape.text_frame.text += contentObject["content"]
        if contentObject["contentType"] == "image":
            slideShape.add_picture(contentObject["imagePath"], pptx.util.Inches(0.5), pptx.util.Inches(1.75))
    prs.save(outputFileName)