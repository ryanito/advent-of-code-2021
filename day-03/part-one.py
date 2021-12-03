data = open('input.txt', 'r')
lines = data.readlines()

gamma = "0b"
epsilon = "0b"

for index, char in enumerate(lines[0]):

    if char == '\n':
        continue

    one = 0
    zero = 0

    for line in lines:
        if line[index] == '1':
            one += 1
        elif line[index] == '0':
            zero += 1

    if one > zero:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))
