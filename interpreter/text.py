import pdfminer
'''
text: Text = {
    "content": str,
    "coordinates": layout_object.bbox
    "pageNumber": int 
}
'''


def isText(layout_object):
    return isinstance(layout_object, pdfminer.layout.LTTextBox)


def Text(layout_object: pdfminer.layout.LTTextBox, pageNumber: int):
    return {
        "content": layout_object.get_text().strip().replace("\n",""),
        "coordinates": layout_object.bbox,
        "pageNumber": pageNumber
    }
    
