import pprint

def parse(input):
    with open(input, "r") as inpt:
        lines = inpt.readlines()

    for i in range(len(lines)):
        lines[i] = [int(c) for c in lines[i].strip("\n")]

    return lines

def checkdir(input, pos):
    visable = False

    rvisbool = True
    lvisbool = True
    tvisbool = True
    bvisbool = True

    tvis = 0
    bvis = 0
    lvis = 0
    rvis = 0
    totalvis = 0

    for top in reversed(range(pos[0])):
        tvis += 1
        if input[top][pos[1]] >= input[pos[0]][pos[1]]:
            tvisbool = False
            break

    for bottom in range(pos[0] + 1, len(input)):
        bvis += 1
        if input[bottom][pos[1]] >= input[pos[0]][pos[1]]:
            bvisbool = False
            break

    for left in reversed(range(pos[1])):
        lvis += 1
        if input[pos[0]][left] >= input[pos[0]][pos[1]]:
            lvisbool = False
            break


    for right in range(pos[1] + 1, len(input[pos[0]])):
        if right == len(input[pos[0]]):
            break
        rvis += 1
        if input[pos[0]][right] >= input[pos[0]][pos[1]]:
            rvisbool = False
            break

    totalvis = rvis * lvis * tvis * bvis
    visable = rvisbool | lvisbool | tvisbool | bvisbool
    return [visable, totalvis]


def solve(input, part):
    trees = 0
    maxscenic = 0
    visability = [[False] * len(input[0]) for _ in range(len(input))]

    for i in range(len(input)):
        for j in range(len(input[i])):
            visability[i][j] = checkdir(input, pos = [i,j])
            if visability[i][j][0]:
                trees += 1
                if visability[i][j][1] > maxscenic:
                    maxscenic = visability[i][j][1]

    if part == "One":
        return trees
    elif part == "Two":
        return trees, maxscenic


if __name__ == '__main__':
    #print(solve(parse("./test"), "One"))
    print(solve(parse("./input"), "Two"))