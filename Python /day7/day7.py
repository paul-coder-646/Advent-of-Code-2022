import pprint


def parse(input):
    with open(input, "r") as input:
        lines = input.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n").split(" ")
        if len(lines[i]) < 3:
            lines[i].insert(0, " ")

    return lines

def solve(instructionlist, part):
    path = ""
    content = {}
    i = 0

    while i < len(instructionlist) -1:
        if instructionlist[i][1] == "cd":
            if instructionlist[i][2] == "..":
                path = "/".join(path.split("/")[:-1])

            elif instructionlist[i][2] == "/":
                path = "/"
            else:
                if path == "/":
                    path = path + instructionlist[i][2]
                else:
                    path = path + "/" + instructionlist[i][2]

            i += 1

        elif instructionlist[i][2] == "ls":
            counter = 0
            for j in range(i+1, len(instructionlist)):
                counter += 1
                if instructionlist[j][0] == " ":
                    if instructionlist[j][1] == "dir":
                        if path not in content:
                            content[path] = []
                        if path + instructionlist[j][2] not in content:
                            if path == "/":
                                content[path + instructionlist[j][2]] = []
                            else:
                                content[path + "/" + instructionlist[j][2]] = []
                    elif instructionlist[j][1] != "dir":
                        if content[path]:
                            content[path].append([instructionlist[j][1], instructionlist[j][2]])
                        else:
                            content[path] = []
                            content[path].append([instructionlist[j][1], instructionlist[j][2]])
                else:
                    break
            i += counter

    sums = {}
    for key, value in content.items():
        sum = 0
        for countvalue in range(len(value)):
            sum += int(value[countvalue][0])
        for i, j in content.items():
            if key in i:
                if key != i:
                    for count in range(len(j)):
                        sum += int(j[count][0])
        sums[key] = sum
    #Actual Game Solution
    if part == "One":
        result = 0
        for key, value in sums.items():
            if value <= 100000:
                result += value

        return result
    if part == "Two":
        freespace = 70000000 - sums["/"]
        result = []
        for key, value in sums.items():
            if value + freespace  >= 30000000:
                result.append(value)

        return min(result)





if __name__ == '__main__':
    #pprint.pprint(solve(parse("./test"), "One"))
    print(solve(parse("./input"), "One"))
    print(solve(parse("./input"), "Two"))


