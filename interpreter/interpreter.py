from pdfminer.layout import LAParams, LTFigure
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import pdfminer

from pdfminer.high_level import extract_pages
import os
from image import writeImage, isImage

def ensureDir(outputDir):
    if not os.path.exists(outputDir): 
        os.makedirs(outputDir) 

def interpret(layout_object):
    if (isImage(layout_object)):
        writeImage(layout_object, "output")
    # recursively parse the layout objects
    if (isinstance(layout_object, pdfminer.layout.LTPage) or isinstance(layout_object, pdfminer.layout.LTContainer)):
        for child in layout_object:
            return interpret(child)
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

    for page in pages:
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            interpret(lobj)
        
interpretMain("test/P5 CW Quesitons.pdf")