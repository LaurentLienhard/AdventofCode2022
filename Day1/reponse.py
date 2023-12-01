#Import data from file puzzle.txt in the current directory
with open('puzzle.txt') as f:
    data = f.readlines()

#read each line and find the first numeric character and the last numeric character. if they are only one numeric character, then the first and last are the same
#add the numeric characters together and print the sum








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


