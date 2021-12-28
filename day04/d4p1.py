def main():

    boards = []
    with open("day04/input.txt") as f:
        nums = f.readline()
        line = f.readline()
        while line:
            board = []
            for i in range(5):
                line = f.readline()
                board.append(line)
            boards.append(boardListToList(board))
            line = f.readline()
    
    nums = list(map(int, nums.split(','))) #fancy~
    
    #nums = list of ints, the numbers in the order that they are "called"
    #boards = list of lists of lists of ints, the boards represendted as all 10 of their win conditions
    
    def findWinner(): #why is this allowed though (I made a fuction to break out of the nested loops)
        for num in nums:
            for board in boards:
                for row in board:
                    if row.count(num) == 1:
                        row.remove(num)
                        if len(row) == 0:
                            sumUnmarked = 0
                            for i in range(5): #if we took all 10 rows there would be duplicates
                                sumUnmarked += sum(board[i])
                            return num * sumUnmarked
    score = findWinner()
    print(score)

def boardListToList(boardStr): #board: list of strings to list of lists of ints
    boardList = []
    for i in range(5): #for the verticals
        boardList.append(list())
    for rowStr in boardStr:
        boardList.append(rowStringToList(rowStr)) #horizontals
        for i in range(5):
            boardList[i].append(int(rowStr[i*3:i*3+2])) #verticals
    return boardList

def rowStringToList(rowStr): #row: string to list of ints
    rowList = []
    for i in range(5):
        rowList.append(int(rowStr[i*3:i*3+2]))
    return rowList

main()