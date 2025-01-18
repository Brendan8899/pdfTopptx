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

def getImage(layout_object):
    if isinstance(layout_object, pdfminer.layout.LTImage):
        return layout_object
    if isinstance(layout_object, pdfminer.layout.LTContainer):
        for child in layout_object:
            return getImage(child)
    else:
        return None



def compileImage(page: pdfminer.layout.LTPage, outputDir: str):
    ensureDir(outputDir)  
    images = list(filter(bool, map(getImage, page)))
    iw = ImageWriter(outputDir)
    for image in images:
        iw.export_image(image)

def compile(inputFile: str):
    fp = open(inputFile, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)

    for page in pages:
        print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        compileImage(layout, "output")
        '''
        for lobj in layout:
            if isinstance(lobj, LTFigure):
                extractedFigure = getImage(lobj)
                print(extractedFigure)

            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                print('At %r is text: %s' % ((x, y), text))
            '''
compile("test/P5 CW Quesitons.pdf")