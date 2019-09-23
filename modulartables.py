# File  : modulartables.py
# Author: Grant J. Bierly (gjb1058)
# Date  : 09/23/2019

import sys

def buildLine(number):
    count = 0
    line = "+"
    while count < (number+1):
        line+="---+"
        count+=1
    return line

def generateHeader(number, OP_CODE):
    header = []
    if(OP_CODE)==1:
        header.append('+')
    elif(OP_CODE)==2:
        header.append('*')
    else:
        print("Invalid OP_CODE")
    for num in xrange(0,number):
        header.append(num)

    return header

# generateTable
# OP_CODE = what operation to do.
#   1:  Addition
#   2:  Multiplication

def generateTable(number, OP_CODE):
    curRow = []
    table = []
    table.append(generateHeader(number, OP_CODE))
    for row in xrange(0,number):
        curRow=[]
        for col in xrange(0,number):
            if OP_CODE == 1:
                value = (row + col) % number
                curRow.append(value)
            elif OP_CODE == 2:
                value = (row * col) % number
                curRow.append(value)
            else:
                print("Invalid Operation. Exiting")
                exit(1)
        table.append(curRow)
    return table

def printTable(table,line):
    print(line)
    rowNum = 0
    for row in table:
        if rowNum!=0:
            print "| "+str(rowNum),
        rowNum+=1
        for val in row:
            print "| "+str(val),
        print("|")
        print(line)
        
if len(sys.argv)!=2:
    print("Invalid Input.")
else:
    number = int(sys.argv[1])
    myLine = buildLine(number)
    addTable = generateTable(number, 1)
    mulTable = generateTable(number, 2)
    printTable(addTable,myLine) 
    print("")
    printTable(mulTable,myLine)
        
