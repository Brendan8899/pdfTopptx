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
                if (len(tables[j]) > 1 and tables[j][0][0] != "" and tables[j][0][0] != None):
                    df = pd.DataFrame(tables[j], columns=tables[j][0])
                    dictionary[i].append(df)
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
def handleFilterRequest(textToProcess, pageNumber):
    two_d_lists = getTablesFromSpecifiedPage(pageNumber)
    final_string_list = getTableStringRepresentation(two_d_lists)
    print("This is the List")
    print(final_string_list)
    if textToProcess in final_string_list:
        return False
    else:
        return True
    
def getTablesFromSpecifiedPage(pageNumber):
    print("Cached Dictionary")
    print(cachedDictionary)
    return cachedDictionary[pageNumber]

def getTableStringRepresentation(two_d_lists):
    listOfFinalString = []
    print("2d Lists")
    print(two_d_lists)
    for two_d_list in two_d_lists:
        for i in range(len(two_d_list[0])):
            for j in range(len(two_d_list)):
                finalString = two_d_list[j][i] + " "
                listOfFinalString.append(finalString)
    return listOfFinalString