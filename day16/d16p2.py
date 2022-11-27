def main():

    with open("day16/input.txt") as f:
        hexi = f.read()
    
    bina = bin(int(hexi, 16))[2:].zfill(len(hexi)*4) #binary string, chop off 0b at front and add back zeros at front
    #print(bina)

    strEq = ""
    eq = []
    endParasLen = []
    endParasNum = []
    depth = 0
    
    i = 0
    while i <= bina.rfind('1'):
        #version = int(bina[i:i+3], 2) #no need for this I guess
        type = int(bina[i+3:i+6], 2)
        i += 6
        if type == 4:
            value = ""
            while int(bina[i]) == 1:
                value += bina[i+1:i+5]
                i += 5
            value += bina[i+1:i+5]
            value = int(value, 2)
            strEq += ' ' + str(value) #eq it was originally a string
            code = "eq"
            for d in range(depth):
                code += "[-1]"
            code += ".append(" + str(value) + ")"
            exec(code) #what a nice niche function
            i += 5 #then big loop starts over
        
        else:
            strEq += '['
            code = "eq"
            for d in range(depth):
                code += "[-1]"
            code += ".append([" + str(type) + "])"
            exec(code)
            depth += 1
            if int(bina[i]) == 0:
                length = int(bina[i+1:i+16], 2)
                i += 16 #loop stars over
                endParasLen.append(i+length)
            else:
                number = int(bina[i+1:i+12], 2)
                i += 12 #and loop stars over
                endParasNum.insert(0, [depth, number]) 
                    #insert because if it is deeper it is resolved first, +1 because it counts down immediately
            strEq += str(type)
        
        if type == 4:
            somethingRemoved = True
            while somethingRemoved:
                somethingRemoved = False
                endParasNum.sort(reverse=True, key=sortByDepth)
                for n in endParasNum: #messy because this depends on depth, oh boi I hope this works
                    if depth == n[0]: #also no stuff never gets deleted from this list but it's fiiiiiiinnneeeeeeee ehehe...
                        n[1] -= 1
                        if n[1] == 0:
                            strEq += ']'
                            depth -= 1
                            #somethingRemoved = True #I MADE A GRAVE MISTAKE ALL I NEEDED TO DO WAS TAKE OUT THIS LINE AAHHHHH
                for l in endParasLen:
                    if i == l:
                        strEq += ']'
                        depth -= 1
                        endParasLen.remove(l)
                        somethingRemoved = True
                        break #will only remove one at a time
        
        
    
    #eq[0] = help
    #print(eq[0])
    #print(strEq)
    #print(endParasNum)
    print(evaluate(eq[0]))

def sortByDepth(n):
    return n[0]

def evaluate(eq):
    if isinstance(eq, int):
        return eq
    else:
        t = eq[0]
        if t == 0:
            sum = 0
            for i in range(1, len(eq)):
                sum += evaluate(eq[i])
            return sum
        elif t == 1:
            product = 1
            for i in range(1, len(eq)):
                product *= evaluate(eq[i])
            return product
        elif t == 2:
            minimum = float("inf")
            for i in range(1, len(eq)):
                minimum = min(minimum, evaluate(eq[i]))
            return minimum
        elif t == 3:
            maximum = 0
            for i in range(1, len(eq)):
                maximum = max(maximum, evaluate(eq[i]))
            return maximum
        elif t == 5:
            if evaluate(eq[1]) > evaluate(eq[2]):
                return 1
            else:
                return 0
        elif t == 6:
            if evaluate(eq[1]) < evaluate(eq[2]):
                return 1
            else:
                return 0
        else: #if t == 7
            if evaluate(eq[1]) == evaluate(eq[2]):
                return 1
            else:
                return 0

main()