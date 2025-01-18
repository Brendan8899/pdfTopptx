from pdfminer.layout import LAParams, LTFigure
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import pdfminer

from pdfminer.high_level import extract_pages
import os
from image import isImage, Image
from text import isText, Text

def ensureDir(outputDir):
    if not os.path.exists(outputDir): 
        os.makedirs(outputDir) 

def interpret(layout_object, pageNumber: int):
    if (isImage(layout_object)):
        print(Image(layout_object, pageNumber))
    if (isText(layout_object)):
        print(Text(layout_object, pageNumber))
        
    # recursively parse the layout objects
    if (isinstance(layout_object, pdfminer.layout.LTPage) or isinstance(layout_object, pdfminer.layout.LTContainer)):
        for child in layout_object:
            return interpret(child, pageNumber)
    else:
        return None


# read input pdf file and convert to PDF Miner layouts
def interpretMain(inputFile: str):
    fp = open(inputFile, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)

    for pageNumber, page in enumerate(pages):
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            interpret(lobj, pageNumber)
        
interpretMain("test/P5 CW Quesitons.pdf")