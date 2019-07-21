# Solution to the practise problem
# https://automatetheboringstuff.com/chapter6/
# Table Printer

def printTable(tableList):
    """Prints the list of list of strings with each column right justified"""
    colWidth = 0
    
    for row in tableList:
        colWidth = max(colWidth, max([len(x) for x in row]))
    colWidth += 1
    printedTable = ''

    tableList = [[row[i] for row in tableList] for i in range(len(tableList[0]))]

    for row in tableList:
        for item in row:
            printedTable += item.rjust(colWidth, ' ')
        printedTable += '\n'
    
    print(printedTable)    

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)