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
    def consumeText(self): 
        '''
        consume until
        1. running out of index
        2. encounter image
        3. encounter different original page
        '''
        def formatContent(payload: str):
            payload = payload.strip()
            if (payload[-1] != '.' or not payload[0].isalnum()):
                return "@(br)" + payload
            else:
                return " " + payload
                
        originalObject = self.contentObjects[self.index]
        currentObject = originalObject
        pageReference = currentObject["pageNumber"]
        currentContent = formatContent(currentObject["content"]) 
                
        # Dark magic ✨
        while (self.peekTrail() or (self.matchTypeNext("text") and self.matchPageNumberNext(pageReference))):
            self.index += 1 # advance
            currentObject = self.contentObjects[self.index]
            # Check if it's the end of the sentence or not
            currentContent += formatContent(currentObject["content"]) 
            
        return {
            "content": currentContent,
            "coordinates": originalObject["coordinates"], # for simplicity
            "pageNumber": originalObject["pageNumber"],
            "contentType": "text"
        }

    
    def run(self):
        table_last_page = None
        while (self.index < len(self.contentObjects)):
            contentObject = self.contentObjects[self.index]
            if (contentObject["contentType"] == "text"):
                maxWordPerPage = config.MAX_WORD_PER_PAGE_DEFAULT
                if self.matchTypeNext("image"):
                    maxWordPerPage =  config.MAX_WORD_PER_PAGE_WITH_IMAGE
                # urge to consume more texts
                else:
                    contentObject = self.consumeText()
                
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
        
    def matchPageNumberNext(self, targetPage: int) -> bool:
        if (self.index + 1 >= len(self.contentObjects)):
            return False
        else:
            return self.contentObjects[self.index + 1]["pageNumber"] == targetPage
        
    def peekTrail(self) -> bool: # handling trailing sentences (e.g. I have [new page] a pen.)
        return self.matchTypeNext("text") and self.contentObjects[self.index]["content"][-1] != "."
    
    def get(self):
        return self.transformedList

def transformMain(contentObjects):
    transformer = Transformer()
    transformer.load(contentObjects)
    transformer.run()
    return transformer.get()    
