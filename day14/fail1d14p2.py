import collections

def main():

    data = []
    steps = 5

    with open("day14/input.txt") as f:
        line = f.readline()
        while line:
            data.append(line.rstrip())
            line = f.readline()
    
    poly = data[0]

    insertions = {}
    for i in range(2, len(data)):
        line = data[i]
        #insertions[line[0:2]] = line[0] + line[6] #+ line[1]
        insertions[line[0:2]] = line[6]
    
    #totals = collections.defaultdict(int)
    #for p in poly:
    #    totals[p] += 1
    
    #for i in range(len(poly)-1):
    #    makeInsertion(poly[i:i+2], insertions, 0, steps, totals)

    for s in range(steps):
        print("step", s+1)
        inserts = ""
        for i in range(len(poly)-1):
            inserts += insertions[poly[i:i+2]]
        for i in range(len(inserts)):
            pos = i*2 + 1
            poly = poly[:pos] + inserts[i] + poly[pos:]
        insertions[poly[0]+poly[-1]] = poly[1:-1]
        insertions[poly[0]+poly[-3]] = poly[1:-3]
        insertions[poly[2]+poly[-1]] = poly[3:-1]
 
    totals = collections.defaultdict(int)
    for p in poly:
        totals[p] += 1

    sortedElements = sorted(totals, key=totals.get) #keys of dict, sorted by their values ?
    print(totals[sortedElements[-1]] - totals[sortedElements[0]])

#def makeInsertion(pair, insertions, step, steps, totals):
#    if step >= steps:
#        print(step)
#        return
#    insert = insertions[pair]
#    totals[insert] += 1
#    makeInsertion(pair[0]+insert, insertions, step+1, steps, totals)
#    makeInsertion(insert+pair[1], insertions, step+1, steps, totals)

main()