import pdfminer
from pdfminer.image import ImageWriter
def writeImage(image: pdfminer.layout.LTImage, outputDir: str):
    iw = ImageWriter(outputDir)
    iw.export_image(image)

def isImage(layout_object):
    return isinstance(layout_object, pdfminer.layout.LTImage) or isinstance(layout_object, pdfminer.layout.LTImage)


def Image(layout_object: pdfminer.layout.LTImage, pageNumber: int):
    return {
        "content": layout_object, # store as pdfminer.layout.LTImage
        "coordinates": layout_object.bbox,
        "pageNumber": pageNumber
    }