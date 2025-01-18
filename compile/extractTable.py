import pdfplumber
import pandas as pd
from tabulate import tabulate

def main():
    with pdfplumber.open("HacknRoll.pdf") as pdf:
        for page in pdf.pages:
            tables = extractTablePerFile(page)
            for table in tables:
                if (len(table) > 1 and table[0][0] != "" and table[0][0] != None):
                    df = pd.DataFrame(table[0:], columns=table[0])  # Use the first row as column names
                    print(tabulate(df, headers='keys', tablefmt='grid'))
                else:
                    pass

def extractTablePerFile(pdfPage):
    tables = pdfPage.extract_tables()
    return tables
    
if __name__ == '__main__':
    main()