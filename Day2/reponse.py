from mailbox import NoSuchMailboxError
from numbers import Number
import re
from webbrowser import get

def getGameNumber(string):
    match = re.search(r'\d+', string)
    if match:
        return int(match.group())
    else:
        return None

def getRedGameColor(string):
    #find all accourance of a regex in a string
    match = re.findall(r'(\d*) red', string)
    return match

def getGreenGameColor(string):
    #find all accourance of a regex in a string
    match = re.findall(r'(\d*) green', string)
    return match

def getBlueGameColor(string):
    #find all accourance of a regex in a string
    match = re.findall(r'(\d*) blue', string)
    return match

def Day1Part1():
    RedCube = 12
    GreenCube = 13
    BlueCube = 14

    with open("Day2/puzzle.txt", "r") as f:
        data = f.readlines()

    sum = 0
    for line in data:
        GameImpossible = False
        GameNumber = ""
        GameNumber = getGameNumber(line)
        #foreach value in getRedGameColor(line): if value is bigger than Redcube, Break
        for value in getRedGameColor(line):
            if int(value) > RedCube:
                GameImpossible = True
                break
        for value in getGreenGameColor(line):
            if int(value) > GreenCube:
                GameImpossible = True
                break
        for value in getBlueGameColor(line):
            if int(value) > BlueCube:
                GameImpossible = True
                break
        if GameImpossible == False:
            sum += GameNumber
    print(sum)

Day1Part1()

def Day1Part2():
    with open("Day2/puzzle.txt", "r") as f:
        data = f.readlines()
    
    sum = 0
    for line in data:
        #foreach value in getRedGameColor(line): if value is bigger than Redcube, Break
        NumberOfRedCube = getRedGameColor(line)
        NumberOfRedCube = list(map(int, NumberOfRedCube))
        NumberOfRedCube.sort()

        NumberOfGreenCube = getGreenGameColor(line)
        NumberOfGreenCube = list(map(int, NumberOfGreenCube))
        NumberOfGreenCube.sort()

        NumberOfBlueCube = getBlueGameColor(line)
        NumberOfBlueCube = list(map(int, NumberOfBlueCube))
        NumberOfBlueCube.sort()

        result = int(NumberOfRedCube[-1]) * int(NumberOfGreenCube[-1]) * int(NumberOfBlueCube[-1])
        sum += result
    print(sum)

Day1Part2()