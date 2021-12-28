def main():
    lines = []
    with open("day03/input.txt") as f:
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()
    
    bits = range(len(lines[-1])) #range of number of bits
    commons = []
    for i in bits:
        commons.append(0) #creates list, length of number of bits, starting with int values of 0
    
    #if bit is 0, subtract 1 from corresponding int in the list 'common'; otherwise, add 1
    #if bit from the list 'common' ends up negative, there were more 0's; otherwise, more 1's
    for line in lines:
        for i in bits:
            if line[i] == '0':
                commons[i] -= 1
            else:
                commons[i] += 1
    
    #idk what to do if number of 0's and 1's are the same
    gammaBinary = ""
    epsilonBinary = ""
    for bit in commons:
        if bit < 0:
            gammaBinary += '0'
            epsilonBinary += '1'
        else:
            gammaBinary += '1'
            epsilonBinary += '0'
    
    gamma = int(gammaBinary, 2)
    epsilon = int(epsilonBinary, 2)
    product = gamma * epsilon
    print(product)

main()