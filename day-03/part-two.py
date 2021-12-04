lines = [[int(x) for x in y] for y in [line.rstrip()
                                       for line in open('input.txt').readlines()]]


def scrub(input, mode):
    lines = input.copy()

    while len(lines) > 1:
        for i in range(len(lines[0])):
            half = len(lines) / 2

            if sum([x[i] for x in lines]) >= half:
                keep = 1
            else:
                keep = 0

            if mode == 0:
                keep = (keep + 1) % 2

            for line in input:
                if (len(lines) > 1) and line[i] != keep and line in lines:
                    lines.remove(line)

    return int(''.join(str(x) for x in lines[0]), 2)


print(scrub(lines, 1) * scrub(lines, 0))
