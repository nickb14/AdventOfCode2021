def main():

    with open("day21/input.txt") as f:
        pos1 = int(f.readline()[28:])
        pos2 = int(f.readline()[28:])
    
    #testing purposes...
    #pos1 = 4
    #pos2 = 8

    #just doing everything twice but don't care it looks fine

    #{turns: unis}, where unis is the number of universes this player took this amount of turns
    p1Possibilities = takeTurn(0, pos1, 0, 1, {})
    p2Possibilities = takeTurn(0, pos2, 0, 1, {})

    #number of turns reverse sorted
    p1Turns = sorted(p1Possibilities)
    p1Turns.reverse()
    p2Turns = sorted(p2Possibilities)
    p2Turns.reverse()

    #{turns: unis}, where unis is the number of universes the other player took more turns, *KINDA*
    p1WinUnis = {}
    p2WinUnis = {}

    totalUnis = 0
    for k in p1Turns:
        #why divide by 27 here? I am not totally sure but I trust my brain logic
        #no but really it is beacuse this is like the potential number of universes
        #it would take this many turns, but if the other player wins before that, many
        #of these universes are not eve being created
        totalUnis = (totalUnis + p1Possibilities[k]) // 27
        p2WinUnis[k-1] = totalUnis
    totalUnis = 0
    for k in p2Turns:
        totalUnis = (totalUnis + p2Possibilities[k]) // 27
        p1WinUnis[k] = totalUnis
    
    p1TotalWins = 0
    p2TotalWins = 0

    for k in p1Turns:
        tempUnis = p1WinUnis.get(k, 0)
        p1TotalWins += p1Possibilities[k] * tempUnis
    for k in p2Turns:
        tempUnis = p2WinUnis.get(k, 0)
        p2TotalWins += p2Possibilities[k] * tempUnis
    
    moreWins = max(p1TotalWins, p2TotalWins)
    print(moreWins)

#revolting
#recursion!
#returns dict, turns:universes, for all possibilities of a single player
def takeTurn(score, pos, turn, unis, allPossibilities):
    possibleDice(score, pos, turn, unis, 3, 1, allPossibilities)
    possibleDice(score, pos, turn, unis, 4, 3, allPossibilities)
    possibleDice(score, pos, turn, unis, 5, 6, allPossibilities)
    possibleDice(score, pos, turn, unis, 6, 7, allPossibilities)
    possibleDice(score, pos, turn, unis, 7, 6, allPossibilities)
    possibleDice(score, pos, turn, unis, 8, 3, allPossibilities)
    possibleDice(score, pos, turn, unis, 9, 1, allPossibilities)

    return allPossibilities

def possibleDice(score, pos, turn, unis, roll, prevUnis, allPossibilities):
    newPos = (pos + roll) % 10
    newScore = score + newPos
    if newPos == 0:
        newScore += 10
    newTurn = turn + 1
    newUnis = prevUnis * unis
    if newScore >= 21: #WIN CONDITION kinda important
        tempUnis = allPossibilities.get(newTurn, 0)
        allPossibilities[newTurn] = tempUnis + newUnis
        return
    takeTurn(newScore, newPos, newTurn, newUnis, allPossibilities)

main()