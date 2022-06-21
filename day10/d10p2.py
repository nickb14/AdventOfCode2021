def main():

    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    points = (None, "(", "[", "{", "<") #index is spoint value
    
    data = []
    with open("day10/input.txt") as f:
        line = f.readline()
        while line:
            data.append(line.rstrip()) #get stripped
            line = f.readline()
    
    scores = []
    for line in data:
        opens = [] #the open brackets, a list of single strings
        for c in line:
            if c in brackets.keys():
                opens.append(c)
            elif brackets[opens[-1]] == c:
                opens.pop(-1)
            else:
                opens = None
                break
        if opens:
            tot = 0
            opens.reverse()
            for b in opens:
                tot = tot*5 + points.index(b)
            scores.append(tot)
    
    scores.sort()
    middle = scores[int(len(scores)/2)]
    print(middle)

main()