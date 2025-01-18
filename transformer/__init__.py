import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import transformer.text
import config

class Transformer:
    def __init__(self):
        self.offset = 0
        self.transformedList = []
    def load(self, contentObjects):
        self.contentObjects = contentObjects
        self.index = 0
    def run(self):
        while (self.index < len(self.contentObjects)):
            contentObject = self.contentObjects[self.index]

            if (contentObject["contentType"] == "text"):
                maxWordPerPage = config.MAX_WORD_PER_PAGE_DEFAULT
                if self.matchTypeNext("image"):
                    maxWordPerPage =  config.MAX_WORD_PER_PAGE_WITH_IMAGE
                results, offset = transformer.text.chopTextObject(contentObject, self.offset, maxWordPerPage)
                for result in results: 
                    self.transformedList.append(result)
                self.offset += offset

            if (contentObject["contentType"] == "image"):
                contentObject["pageNumber"] +=  self.offset
                self.transformedList.append(contentObject)
            
            if (contentObject["contentType"] == "table"):
                contentObject["pageNumber"] += self.offset
                self.transformedList.append(contentObject)
            self.index += 1
            
    def matchTypeNext(self, targetType: str) -> bool:
        if (self.index + 1 >= len(self.contentObjects)):
            return False
        else:
            return self.contentObjects[self.index + 1]["contentType"] == targetType
        
    def get(self):
        return self.transformedList

def transformMain(contentObjects):
    transformer = Transformer()
    transformer.load(contentObjects)
    transformer.run()
    return transformer.get()    
