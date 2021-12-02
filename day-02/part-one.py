data = open('input.txt', 'r')
lines = data.readlines()

horizontal = 0
depth = 0

for line in lines:
    split = line.split()
    direction = split[0]
    number = int(split[1])
    
    if (direction == 'forward'):
        horizontal += number
    elif (direction == 'down'):
        depth += number
    elif (direction == 'up'):
        depth -= number

print(horizontal * depth)