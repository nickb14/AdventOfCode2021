def main():

    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
        "\n": 0 #maybe not the best solution, but just so it doesn't freak out when it reaches the end of a line
    }
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    
    data = []
    with open("day10/input.txt") as f:
        line = f.readline()
        while line:
            data.append(line)
            line = f.readline()
    
    tot = 0
    for line in data:
        temp = []
        for c in line:
            if c in brackets.keys():
                temp.append(c)
            elif brackets[temp[-1]] == c:
                temp.pop(-1)
            else:
                tot += points[c]
                break
    
    print(tot)

main()