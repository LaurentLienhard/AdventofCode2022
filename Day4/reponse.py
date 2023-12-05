import re

def Day4part1():
    with open("Day4/puzzle.txt", "r") as f:
        data = f.readlines()

    sum = 0
    for line in data:
        occurence = 0
        #print('Line : ' + line)
        winningNumbers = ''
        allNumbers = ''
        winningNumbers = SplitLineWinner(line)
        allNumbers = SplitLineAllNumbers(line)
        #print("Winner Numbers : " + winningNumbers )
        #print("All Numbers : " + allNumbers)
        winningNumbers = ReturnDigit(winningNumbers)
        allNumbers = ReturnDigit(allNumbers)
        for number in winningNumbers:
            if number in allNumbers:
                occurence += 1
                #print('occurence : ' , occurence) 
        
        sum += (2 ** (occurence -1))
    print('Sum : ' ,sum)



def SplitLineWinner(line):
    result = line.split(':')
    result = result[1].split('|')
    return result[0]

def SplitLineAllNumbers(line):
    result = result = line.split('|')
    return result[-1]

def ReturnDigit(string):
    match = re.findall(r'(\d+)', string)
    return match

def GetValueOccurence(valeur):
    i=1
    resultat = 1
    while i < valeur:
        resultat = resultat * 2
        i = i +1
    return resultat

Day4part1()