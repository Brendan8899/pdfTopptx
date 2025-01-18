import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import pdfTopptx.interpreter
import pdfTopptx.transformer
import pdfTopptx.assembler
import pdfTopptx.config as config
import shutil

def removeTmp():
    try:
        shutil.rmtree(config.TMP_DIRECTORY)
    except:
        pass
# Main handler
def convert(input_file: str, output_file: str, title = "", subtitle = "", 
            paragraphFontSize = 18, fontFamily = "Calibri", maxWordPerPageDefault = 70, maxWordPerPageWithImage = 30,
            ignoreTop = 0, ignoreBottom = 0):
    
    config.TITLE = title
    config.SUBTITLE = subtitle

    config.INPUT_FILENAME = input_file
    config.OUTPUT_FILENAME = output_file
    
    config.FONT_FAMILY = fontFamily
    config.PARAGRAPH_FONT_SIZE = paragraphFontSize
    config.MAX_WORD_PER_PAGE_DEFAULT = maxWordPerPageDefault
    config.MAX_WORD_PER_PAGE_WITH_IMAGE = maxWordPerPageWithImage

    config.IGNORE_TOP = ignoreTop
    config.IGNORE_BOTTOM = ignoreBottom
    removeTmp()
    contentObjectList = interpreter.interpretMain(config.INPUT_FILENAME)
    contentObjectList = transformer.transformMain(contentObjectList)
    assembler.assemble(contentObjectList, config.OUTPUT_FILENAME)
    removeTmp()