def main():

    with open("/workspace/AdventOfCode2021/day4/input.txt") as f:
        nums = f.readline()
        line = f.readline()
        while line:
            board = []
            for i in range(5):
                line = f.readline()
                board.append(line)
            #make board into a list of 10 sets of 5
            #put list into longr list? (or should I be uning lists idk)
            line = f.readline()
    
    print(board)
    print(boardListToList(board))

#this system very much does not work right now
def boardListToList(boardStr): #list of strings to list of lists of ints
    boardList = []
    for row in boardStr:
        boardList.append(rowStringToList(row))
    return boardList

def rowStringToList(rowStr): #string to list of ints
    rowList = []
    for i in range(5):
        rowList.append(int(rowStr[i*3:i*3+2]))
    return rowList

main()