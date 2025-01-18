import pdfminer
import typing

class Text(typing.TypedDict):
    content: str
    coordinates: tuple[float] # follows layout_object.bbox
    pageNumber: int


def isText(layout_object):
    return isinstance(layout_object, pdfminer.layout.LTTextBox)


def Text(layout_object: pdfminer.layout.LTTextBox, pageNumber: int) -> Text:
    return {
        "content": layout_object.get_text().strip().replace("\n",""),
        "coordinates": layout_object.bbox,
        "pageNumber": pageNumber
    }
    
