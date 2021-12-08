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

main()