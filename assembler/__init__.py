import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pptx import Presentation
from pptx.util import Inches
# ContentObject := Text | Image | ...
# Assume that objectList is sorted by page & coordinates

# Version 1
def assemble(contentObjectList, outputFileName): # [] ContentObject
    contentObjectList.sort(key = lambda a: a["pageNumber"])
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
    prs.save(outputFileName)