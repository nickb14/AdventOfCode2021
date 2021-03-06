def main():

    with open("day21/input.txt") as f:
        pos1 = int(f.readline()[28:])
        pos2 = int(f.readline()[28:])

    score1 = 0
    score2 = 0
    turn1 = True
    dice = 6 #the sum of 3 rolls, kinda basically

    while True:
        if turn1:
            pos1 = (pos1 + dice) % 10
            score1 += pos1
            if pos1 == 0:
                score1 += 10
            if score1 >= 1000:
                loser = score2
                break
            turn1 = False
        else:
            pos2 = (pos2 + dice) % 10
            score2 += pos2
            if pos2 == 0:
                score2 += 10
            if score2 >= 1000:
                loser = score1
                break
            turn1 = True
        dice += 9

    diceRolls = dice // 3 + 1
    print(diceRolls * loser)

main()