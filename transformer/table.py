import config

def addTableToNextPage(contentObjectList, incomingTable):
    elementsInSamePage = list(filter(filterFunction(incomingTable), contentObjectList))
    if len(elementsInSamePage) != 0:
        return True
    else:
        return False
    
def filterFunction(incomingTable):
    def innerFilter(contentObject):
        return contentObject["pageNumber"] == incomingTable["pageNumber"]
    return innerFilter