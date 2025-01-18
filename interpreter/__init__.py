from pdfminer.layout import LAParams, LTFigure
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
import pdfminer

from pdfminer.high_level import extract_pages
import os

from interpreter.image import isImage, createImage
from interpreter.text import isText, createText
from interpreter.table import extractedTableByPage, createTable
import config

def interpret(layout_object, pageNumber: int, contentObjectList):
    outputDir = config.TMP_DIRECTORY
    if (isImage(layout_object)):
        contentObjectList.append(createImage(layout_object, outputDir, pageNumber))
    if (isText(layout_object)):
        contentObjectList.append(createText(layout_object, pageNumber))
        
    # recursively parse the layout objects
    if (isinstance(layout_object, pdfminer.layout.LTPage) or isinstance(layout_object, pdfminer.layout.LTContainer)):
        for child in layout_object:
            return interpret(child, pageNumber, contentObjectList)
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
    contentObjectList = []
    extractedTables = extractedTableByPage(inputFile)
    for pageNumber, page in enumerate(pages):
        # list(map(extractedTables[pageNumber]))
        tablesInPage = extractedTables[pageNumber]
        for j in range(len(tablesInPage)):
            contentObjectList.append(createTable(tablesInPage[j], j, pageNumber))
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            interpret(lobj, pageNumber, contentObjectList)
    
    return contentObjectList
        
