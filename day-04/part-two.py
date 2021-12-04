with open("input.txt") as f:
    numbers = f.readline().strip().split(',')
    cards = [[[[x, False] for x in line.split()] for line in card.split('\n')]
             for card in f.read().strip().split('\n\n')]

winners = []
scores = []


def winner(card, number):

    winners.append(card)

    score = 0
    for row in card:
        for col in row:
            if col[1] == False:
                score += int(col[0])

    scores.append(score * int(number))


for number in numbers:
    for card in cards:

        won = False
        for row in card:

            if won:
                break

            horizontalMatches = 0

            for key, col in enumerate(row):
                # Match found!
                if col[0] == number:
                    col[1] = True

                if col[1]:
                    horizontalMatches += 1

                # Check vertical matches
                verticalMatches = 0
                for row2 in card:
                    if row2[key][1]:
                        verticalMatches += 1

                if horizontalMatches == len(row) or verticalMatches == len(row):
                    if card not in winners:
                        winner(card, number)
                        won = True
                        break

print(scores[-1])
