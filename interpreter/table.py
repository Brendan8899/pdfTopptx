import pdfplumber
import pandas as pd
from tabulate import tabulate

def extractedTableByPage(inputFile):
    dictionary = {}
    with pdfplumber.open(inputFile) as pdf:
        for i in range(len(pdf.pages)):
            dictionary[i] = []
            tables = extractTablePerFile(pdf.pages[i])
            for j in range(len(tables)):
                if (len(tables[j]) > 1 and tables[j][0][0] != "" and tables[j][0][0] != None):
                    df = pd.DataFrame(tables[j], columns=tables[j][0])
                    dictionary[i].append(df)
                    print(tabulate(df, headers='keys', tablefmt='grid'))
                else:
                    pass
    return dictionary

def extractTablePerFile(pdfPage):
    tables = pdfPage.extract_tables()
    return tables

def createTable(dataframe, ordering, pageNumber):
    return {
        "dataFrame": dataframe,
        "ordering": ordering,
        "pageNumber": pageNumber,
        "contentType": "table"
    }