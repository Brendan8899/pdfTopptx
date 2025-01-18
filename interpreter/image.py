import pdfminer
from pdfminer.image import ImageWriter
def writeImage(image: pdfminer.layout.LTImage, outputDir: str):
    iw = ImageWriter(outputDir)
    iw.export_image(image)

def isImage(layout_object):
    return isinstance(layout_object, pdfminer.layout.LTImage)
