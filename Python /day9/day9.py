from pprint import pprint
import copy

def parseInput(input):
    with open(input) as inputfile:
        output = [[a, int(b)] for a, b in (item.split() for item in inputfile.readlines())]
        return output
    
def boundaryCheck(input):
    U = 0
    D = 0
    L = 0
    R = 0
    for i, instruction in enumerate(input):
        match instruction[0]:
            case "U":
                U += instruction[1]
            case "D":
                D += instruction[1]
            case "L":
                L += instruction[1]
            case "R":
                R += instruction[1]

    return max(U, D, L, R)


def tailPosition(pos):
    # The Tail Direction in Compass Direction decides the return parameter
    if pos[0][0] == pos[1][0] and pos[0][1] == pos[1][1]:
        return "On-Top"
    elif pos[0][0] == pos[1][0] and pos[0][1] > pos[1][1]:
        return "N"
    elif pos[0][0] == pos[1][0] and pos[0][1] < pos[1][1]:
        return "S"
    elif pos[0][0] > pos[1][0] and pos[0][1] == pos[1][1]:
        return "W"
    elif pos[0][0] < pos[1][0] and pos[0][1] == pos[1][1]:
        return "E"
    elif pos[0][0] < pos[1][0] and pos[0][1] > pos[1][1]:
        return "NE"
    elif pos[0][0] > pos[1][0] and pos[0][1] < pos[1][1]:
        return "SW"
    elif pos[0][0] < pos[1][0] and pos[0][1] < pos[1][1]:
        return "SE"
    elif pos[0][0] > pos[1][0] and pos[0][1] > pos[1][1]:
        return "NW"

def updatePosition(oldpos, dir):
    # position is [Head,Tail] where Head and Tail are [x,y] 
    #if any(1 for num in oldpos[0] if num < 0) or any( 1 for num in oldpos[0] if num < 0):
     #   raise ValueError(f"Invalid position: {oldpos}")
    
    newpos = copy.deepcopy(oldpos)
    match dir:
        # In all unmentioned cases, the tail stays at its place for that turn
        
        case "U": # Means in our case right
            match tailPosition(oldpos):
                case "W":
                    newpos[1][0] += 1
                case "NW":
                    newpos[1][0] += 1
                    newpos[1][1] += 1
                case "SW":    
                    newpos[1][0] += 1
                    newpos[1][1] -= 1
            newpos[0][0] +=1

        case "D": # Means in our case left
            match tailPosition(oldpos):
                case "E":
                    newpos[1][0] -= 1
                case "NE":
                    newpos[1][0] -= 1
                    newpos[1][1] += 1
                case "SE":    
                    newpos[1][0] -= 1
                    newpos[1][1] -= 1
            newpos[0][0] -=1

        case "L": # Means in our case up
            match tailPosition(oldpos):
                case "S":
                    newpos[1][1] -= 1
                case "SE":
                    newpos[1][0] -= 1
                    newpos[1][1] -= 1
                case "SW":
                    newpos[1][0] += 1
                    newpos[1][1] -= 1
            newpos[0][1] -=1
        case "R": # Means in our case down
            match tailPosition(oldpos):
                case "N":  
                    newpos[1][1] += 1
                case "NE":    
                    newpos[1][0] -= 1
                    newpos[1][1] += 1
                case "NW": 
                    newpos[1][0] += 1
                    newpos[1][1] += 1
            newpos[0][1] +=1
            
    return newpos

def taskOne(input):
    newpos = 1
    positions = []
    inputlist = parseInput(input)
    pos = [[0,0],[0,0]]
    positions.append(pos[1])
    for dir, iterations in inputlist:
        for _ in range(iterations):
            pos = updatePosition(pos, dir)
            x, y = pos[1]
            if pos[1] not in positions:
                positions.append(pos[1])
                newpos +=1
    print(newpos)

def taskTwo(input):
    rope = []
    positions = []

    for i in range(10):
        rope.append([0,0])

    inputlist = parseInput(input)
    for dir, iterations in inputlist:
        for _ in range(iterations):
            for i in range(len(rope)):
                rope[i] = rope[i-1]
                rope[0] = updatePosition([rope[0],rope[1]], dir)
                
                if rope[9] not in positions:
                    positions.append(rope[9])
    print(len(positions))

#taskOne("input9.txt")
taskTwo("test9_2.txt")