
def Day7Part1():
    with open("Day7/puzzle.txt", "r") as f:
        data = f.readlines()

        #order the data by alphabetical order
        data.sort()
        #convert data to an array
        data = [x.strip() for x in data]
        print(data)


def five_of_a_kind(string):
    for i in range(len(string) - 4):
        if string[i] == string[i+1] == string[i+2] == string[i+3] == string[i+4]:
            return True
    return False


Day7Part1()