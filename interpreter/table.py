import pdfplumber
import pandas as pd
from tabulate import tabulate

def extractedTableByPage(inputFile):
    dictionary = {}
    global cachedDictionary 
    with pdfplumber.open(inputFile) as pdf:
        for i in range(len(pdf.pages)):
            dictionary[i] = []
            tables = extractTablePerFile(pdf.pages[i])
            for j in range(len(tables)):
                if (len(tables[j]) > 1 and tables[j][0] != "" and tables[j][0] != None):
                    dictionary[i].append(tables[j])
                else:
                    pass
    cachedDictionary = dictionary
    return dictionary

def extractTablePerFile(pdfPage):
    tables = pdfPage.extract_tables()
    return tables

def createTable(dataframe, ordering, pageNumber):
    return {
        "coordinates": (0,0,0,0),
        "dataFrame": dataframe,
        "ordering": ordering,
        "pageNumber": pageNumber,
        "contentType": "table"
}
    
def handleFilterRequest(contentObject):
    print("Should Reach Here")
    print(contentObject)
    if contentObject["contentType"] != "text":
        return True
    print("Table Should Reach Here")
    print(contentObject)
    textToProcess = contentObject["content"]
    pageNumber = contentObject["pageNumber"]
    three_d_lists = getTablesFromSpecifiedPage(pageNumber)
    final_string_list = getTableStringRepresentation(three_d_lists)
    if textToProcess in final_string_list:
        return False
    else:
        return True
    
def getTablesFromSpecifiedPage(pageNumber):
    return cachedDictionary[pageNumber]

def getTableStringRepresentation(three_d_lists):
    listOfFinalString = []
    for two_d_list in three_d_lists:
        for i in range(len(two_d_list[0])):
            finalString = ""
            for j in range(len(two_d_list)):
                finalString += two_d_list[j][i] + " "
            finalString = finalString.strip()
            listOfFinalString.append(finalString)
    return listOfFinalString