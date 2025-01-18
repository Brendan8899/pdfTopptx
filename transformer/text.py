import re, math

def chopText(text, maxWordPerPage = 30):
    wordCount = len(text.split())
    numberChunk = math.floor(wordCount / maxWordPerPage)
    wordCutOff = maxWordPerPage
    if numberChunk > 0:
        wordCutOff = math.ceil(wordCount / numberChunk) 
        
    sentence_boundary_pattern = r'(?<=[.!?])\s+'
    sentences = re.split(sentence_boundary_pattern, text)
    cumulatedWordCount = 0
    cumulatedSentence = []
    cumulatedTmp = []
    for sentence in sentences:
        cumulatedTmp.append(sentence)
        cumulatedWordCount += len(sentence.split())
        if (cumulatedWordCount >= wordCutOff):
            cumulatedWordCount = 0
            cumulatedSentence.append(' '.join(cumulatedTmp))
            cumulatedTmp = []
    if (len(cumulatedTmp) != 0):
        cumulatedSentence.append(' '.join(cumulatedTmp))
    return cumulatedSentence

def chopTextObject(textObject, initialOffset = 0):
    chopedSentence = chopText(textObject["content"])
    offset = len(chopedSentence) 
    return [
    {
        "content": sentence,
        "coordinates": textObject["coordinates"],
        "pageNumber": textObject["pageNumber"] + indexOffset + initialOffset,
        "contentType": "text"
    }
        for indexOffset, sentence in enumerate(chopedSentence)
    ], offset



