def main():

    total = 0

    with open("day08/input.txt") as f:
        line = f.readline()
        while line:

            i = line.index('|') + 2 #oddly placed logic but whatever
            outputs = line[i:].split()
            for o in outputs:
                s = len(o)
                if s != 5 and s != 6:
                    total += 1

            line = f.readline()
    
    print(total)

main()