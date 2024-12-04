import re

lines = open('day-3/input.txt').read()
total = 0
enable = True

for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)",lines):
    if match == 'do()':
       enable = True

    elif match == "don't()":
       enable = False
  
    elif enable:
        x,y  = map(int,match[4:-1].split(",")) 
        total += x*y
print(total)