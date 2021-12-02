data = open('input.txt', 'r')
lines = data.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    split = line.split()
    direction = split[0]
    number = int(split[1])
    
    if (direction == 'forward'):
        horizontal += number
        depth += aim * number
    elif (direction == 'down'):
        aim += number
    elif (direction == 'up'):
        aim -= number

print(horizontal * depth)