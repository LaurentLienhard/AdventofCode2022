import re

# Day1/Part1
#Import data from file puzzle.txt in the current directory
with open('puzzle.txt') as f:
    data = f.readlines()

sum = 0
for line in data:
    first_num = ""
    last_num = ""
    result = ""
    for i in range(0,len(line)):
        if line[i].isdigit():
            first_num = int(line[i])
            print("first_Num : ", first_num)
            break
    for i in range(len(line)-1,0,-1):
        if line[i].isdigit():
            last_num = int(line[i])
            print("last_Num : ",  last_num)
            break
    #check if last_num is empty 
    if last_num == "":
        last_num = first_num
    #concatenate first_num and last_num to make a number
    result = int(str(first_num) + str(last_num))
    print("result : ", result)
    sum = sum + result
print("sum : ", sum)


# Day1/Part2
arr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pattern = "|".join(arr)
regex = re.compile(pattern)

def ConvertToNumeric(value):
    switcher = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    return switcher.get(value, "Invalid value")

sum = 0
for line in data:
    # Test the regex pattern
    matches = regex.findall(line)
    # if matches is not a digit convert to numeric
    if not matches[0].isdigit():
        matches[0] = ConvertToNumeric(matches[0])
    if not matches[-1].isdigit():
        matches[-1] = ConvertToNumeric(matches[-1])
    result = int(matches[0] + matches[-1])
    print("line : ", line)
    print("matches 0: ", matches[0])
    print("matches -1: ", matches[-1])
    print("result : ", result)
    sum = sum + result
print("sum : ", sum)


