from math import fabs
import re

def Day3part1():
    print("Day3 part1")

    # Read all the data from the file
    file = open("Day3/test.txt", "r")
    data = file.read()

    sum = 0
    # Find all numbers in the data
    numbers = re.findall(r'\d+', data)
    for number in numbers:
        for digit_position, digit in enumerate(number):
            digital_ablolute_position = data.index(number) + digit_position

            if (not (re.search(r'[0-9. ]', data[digital_ablolute_position - 1]))) or (not (re.search(r'[0-9. ]', data[digital_ablolute_position + 1]))):
                print('Number : '  + number)
                print('Digit : ' + digit)
                print('charactere before digit : ' + data[digital_ablolute_position - 1])
                print('charactere after digit : ' + data[digital_ablolute_position + 1])
                print('not Point or digit before digit')
                sum += int(number)
    print('sum : ' + str(sum))

    
Day3part1()