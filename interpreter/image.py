import pdfminer
import typing
from pdfminer.image import ImageWriter
from pdfminer.layout import LTImage
from os import path

def writeImage(image: LTImage, outputDir: str):
    iw = ImageWriter(outputDir)
    fileName = iw.export_image(image)
    return path.join(outputDir, fileName)

def isImage(layout_object):
    return isinstance(layout_object, LTImage) or isinstance(layout_object, LTImage)


class Image(typing.TypedDict):
    imagePath: LTImage
    coordinates: tuple[float] # follows layout_object.bbox
    pageNumber: int
    contentType: str
    
    
def createImage(layout_object: LTImage, outputDir: str, pageNumber: int) -> Image:
    # save image
    imagePath = writeImage(layout_object, outputDir)
    return {
        "imagePath": imagePath, # store as pdfminer.layout.LTImage
        "coordinates": layout_object.bbox,
        "pageNumber": pageNumber,
        "contentType": "image"
    }