def parse(textinput):
    with open(textinput, "r") as input:
        lines = input.readlines()

        for i in range(len(lines)):
            lines[i] = list(map(lambda x: list(map(int, x.split("-"))), lines[i].strip().split(",")))
    return lines

def solve(input, part):
    result = 0
    for val in input:
        if part == "one":
            if (val[0][0] >= val[1][0] and val[0][1] <= val[1][1]) or (val[0][0] <= val[1][0] and val[0][1] >= val[1][1]):
                result += 1
        if part == "two":
            if not(val[0][1] < val[1][0] or val[1][1] < val[0][0]):
                result += 1
    return result

if __name__ == '__main__':
    #print(solve(parse("./input"), "one"))
    print(solve(parse("./input"), "two"))