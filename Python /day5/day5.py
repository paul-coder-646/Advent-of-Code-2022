import copy

def parse(input):
    maxsize = 0
    stacks = []
    tempstack = []
    stacknum = 0
    semistack = []
    finstack = []
    instruct = []

    with open(input, "r") as readfile:
        lines = readfile.readlines()

    copylines = copy.deepcopy(lines)
    # find the number of stacks
    for i in range(len(copylines)):
        copylines[i] = copylines[i].strip(" ").strip("\n")
        try:
            stacks = list(map(int, "".join(copylines[i].split())))
            stacknum = stacks[-1]
            break

        except ValueError:
            maxsize += 1
            continue

    for num in range(maxsize):
        tempstack = []
        lines[num] = list(lines[num].strip("\n"))
        if len(lines) % 2 != 0:
            lines[num].append(" ")

        while len(lines[num]) < stacknum * 4:
            lines[num].append(" ")


        stacklen = len(lines[num])

        for i in range(stacklen // 4):
            tempstack.append(lines[num][4 * i + 1])


        semistack.append(tempstack)

    tempstack = []

    #finally :D we can construct the individual Stacks...
    for width in range(len(semistack[0])):
        for length in range(len(semistack)):
            if semistack[length][width] != " ":
                tempstack.append(semistack[length][width])
        tempstack = list(reversed(tempstack))
        finstack.append(tempstack)
        tempstack = []


    instruct = lines[maxsize+2:]

    return finstack, instruct

def solve(input, instruct, part):
    out = []
    for i in range(len(instruct)):
        instruct[i] = instruct[i].strip("\n").split(" ")
        # pos 1: how many pieces should be moved
        # pos 2: from where should pieces be moved
        # pos 3: where to?
        if part == "one":
            for _ in range(int(instruct[i][1])):
                element = input[int(instruct[i][3])-1].pop()
                input[int(instruct[i][5])-1].append(element)
        if part == "two":
            elements = []
            for _ in range(int(instruct[i][1])):
                elements.append(input[int(instruct[i][3])-1].pop())
            input[int(instruct[i][5])-1] = input[int(instruct[i][5])-1] + elements[::-1]

    for j in range(len(input)):
        if input[j]:
            out.append(input[j][-1])

    return "".join(out)

if __name__ == '__main__':
    #print(solve(*parse("./test"), "one"))
    #print(solve(*parse("./input"), "one"))
    print(solve(*parse("./input"), "two"))
