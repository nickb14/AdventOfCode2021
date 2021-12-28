def main():
    
    maxim = 0
    vents = []

    with open("day05/input.txt") as f:
        line = f.readline()
        while line:
            line = splitInto4(line)
            if line[0] == line[2] or line[1] == line[3]: #only verticals or horizontals
                vents.append(line)
            num = max(line) #find max value- is there better way to do it...?
            if num > maxim: maxim = num
            line = f.readline()
    
    maxim += 1 #EEK I should have just set it to 1000
    graph = []
    for a in range(maxim): #I have suffered
        graph.append([])
        for b in range(maxim):
            graph[a].append(0)

    for vent in vents:
        x1 = vent[0] #uglyyy
        y1 = vent[1] #
        x2 = vent[2] #
        y2 = vent[3] #
        if x1 == x2: #also I wonder if even this solution is too java-y
            if y1 > y2: y1, y2 = y2, y1 #I HATE YOU
            for y in range(y1, y2+1):
                graph[x1][y] += 1
        else:
            if x1 > x2: x1, x2 = x2, x1 #YOU TOO
            for x in range(x1, x2+1):
                graph[x][y1] += 1
    
    total = 0
    for row in graph: # die
        for number in row:
            if number > 1:
                total += 1
    print(total)

def splitInto4(lineStr): #returns list of 4 ints
    temp = lineStr.split(" -> ")
    lineList = []
    for line in temp:
        lineList += line.split(',')
    lineList = list(map(int, lineList))
    return lineList

main()