def main():

    with open("day17/input.txt") as f:
        line = f.read()
    
    xdotdot = line.find("..")
    yequals = line.rfind("y=")
    ydotdot = line.rfind("..")

    xmin = int(line[15:xdotdot])
    xmax = int(line[xdotdot+2:yequals-2])
    ymin = int(line[yequals+2:ydotdot])
    ymax = int(line[ydotdot+2:])
    
    vxmin = 0
    for x in range(xmin):
        vxmin += x
        if vxmin > xmin:
            vxmin = x
            break
    vxmax = xmax
    vymin = ymin
    vymax = ymin*-1-1 #pretty sure this works as long as ymin is nagative

    total = 0
    for vx in range(vxmin, vxmax+1): #including vxmax and vymax
        for vy in range(vymin, vymax+1):
            x, y = 0, 0
            vxt, vyt= vx, vy
            while x <= xmax and y >= ymin: #again assuming ymin is negative
                if x >= xmin and y <= ymax: #if it is in target...
                    total += 1
                    break
                x += vxt
                y += vyt
                if vxt != 0: #and everything is based on positive x velocity, I think
                    vxt -= 1
                vyt -= 1

    print(total)

main()