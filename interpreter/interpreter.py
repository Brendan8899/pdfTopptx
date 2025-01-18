from pdfminer.layout import LAParams, LTFigure
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import pdfminer
from pdfminer.image import ImageWriter
from pdfminer.high_level import extract_pages
import os

def ensureDir(outputDir):
    if not os.path.exists(outputDir): 
        os.makedirs(outputDir) 


def writeImage(image: pdfminer.layout.LTImage, outputDir: str):
    iw = ImageWriter(outputDir)
    iw.export_image(image)

def isImage(layout_object):
    return isinstance(layout_object, pdfminer.layout.LTImage)

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