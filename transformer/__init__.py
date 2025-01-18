import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import transformer.text

# offsetBox is used to pass by reference
def transform(contentObject, transformedList, offsetBox = [0]):
    if (contentObject["contentType"] == "text"):
        results, offset = transformer.text.chopTextObject(contentObject, offsetBox[0])
        for result in results: 
            transformedList.append(result)
        offsetBox[0] += offset
        
    if (contentObject["contentType"] == "image"):
        contentObject["pageNumber"] += offsetBox[0]
        transformedList.append(contentObject)
        offsetBox[0] += 1
        # do absolutely nothing! 
        
    return transformedList

def transformMain(contentObjects):
    transformedList = []
    offsetBox = [0]
    for contentObject in contentObjects:
        transform(contentObject, transformedList , offsetBox)
    transformedList.reverse()
    return transformedList    
