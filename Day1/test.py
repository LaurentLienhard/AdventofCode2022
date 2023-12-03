import re

result = "test"
string = "aeigthtwone"
pattern = re.compile(r"one|two")

while result:
    result = re.search(pattern, string)
    if result:
        print(result)
    else:
        break

