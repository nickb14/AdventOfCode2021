def main():

    sum = 0

    with open("/workspace/AdventOfCode2021/day08/input.txt") as f:
        line = f.readline()
        while line:

            lineList = line.split()
            signals = lineList[:10]
            outputs = lineList[11:]

            key = decode(signals) #euhg

            key = list(map(alphabetizeStr, key)) #for easier comparisons
            outputs = list(map(alphabetizeStr, outputs))

            num = ""
            for output in outputs:
                digit = key.index(output)
                num += str(digit)
            
            sum += int(num)

            line = f.readline()
    
    print(sum)

# returns the list of 10 strings, 
# so that the indexes correspond to the number each string represents
def decode(signals): 
    signals.sort(key = len) #oops modifying the argument? without warning
    key = [''] * 10

    key[1] = signals[0]
    key[4] = signals[2]
    key[7] = signals[1]
    key[8] = signals[9]

    c = key[1][0] #c and f interchangable for these purposes...
    f = key[1][1]
    bd = key[4].replace(c, '').replace(f, '') #ugly just removing
    b = bd[0] #bd also interchangable
    d = bd[1]

    for i in range(3, 6): #signals of length 5
        sig = signals[i]
        if key[3] == '' and c in sig and f in sig:
            key[3] = sig
        elif key[5] == '' and b in sig and d in sig:
            key[5] = sig
        else:
            key[2] = sig
    
    for i in range(6, 9): #signals of length 6
        sig = signals[i]
        if key[6] == '' and (c not in sig or f not in sig):
            key[6] = sig
        elif key[9] == '' and b in sig and d in sig:
            key[9] = sig
        else:
            key[0] = sig
    
    return key

def alphabetizeStr(str):
    return ''.join(sorted(str))

main()