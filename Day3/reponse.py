import re

def Day3part1():
    print("Day3 part1")

    # Read all the data from the file
    file = open("Day3/puzzle.txt", "r")
    data = file.read()

    # Find all numbers in the data
    numbers = re.findall(r'\d+', data)

    # Check if each digit of the number is adjacent to a symbol different than a point
    for number in numbers:
        for digit in number:
            print(number)
            print(digit)
Day3part1()