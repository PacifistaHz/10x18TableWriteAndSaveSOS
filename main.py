import random

def createSOSTable(column, line):
    letters=["S","O"]
    array=[[0]*column for i in range(line)]
    result=""
    for i in range(0,line):
        for j in range(0,column):
            randomLetter=random.sample(letters,1)
            array[i][j]=randomLetter[0]
            result=result+randomLetter[0]+"\t"
        result+="\n"
    return {"Result":result, "Array":array}

def saveFile(fileName, text):
    with open(fileName + ".txt", "w") as f:
        f.write(text)

tableOfSOS = createSOSTable(6, 10)["Result"]
saveFile("sos", tableOfSOS)
print(tableOfSOS)
