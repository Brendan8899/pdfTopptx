import pdfminer
import typing
from pdfminer.layout import LAParams, LTTextBox 
import config


class Text(typing.TypedDict):
    content: str
    coordinates: tuple[float] # follows layout_object.bbox
    pageNumber: int
    contentType: str


def isText(layout_object):
    return isinstance(layout_object, LTTextBox)


def createText(layout_object: LTTextBox, pageNumber: int) -> Text:
    return {
        "content": layout_object.get_text().strip().replace("\n"," "),
        "coordinates": layout_object.bbox,
        "pageNumber": pageNumber,
        "contentType": "text"
    }
    
def handleFilterRequestText(width: float, height: float):
    def handler(contentText):
        return contentText["coordinates"][1] < height - config.IGNORE_TOP and contentText["coordinates"][1] > config.IGNORE_BOTTOM

    return handler