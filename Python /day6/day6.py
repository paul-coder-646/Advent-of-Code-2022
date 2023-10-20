def parse(input):
    with open(input, "r") as inp:
        line = [*inp.readline()]
    return line

def solve(input, part):
    if part == "one":
        window = 4
    elif part == "two":
        window = 14

    pos = 0
    seen = []
    unique = False
    windowarr = [0] * window
    for j in range(0, len(input) - window):
        unique = True
        for i in range(window):
            windowarr[i] = input[j+i]

        for place in windowarr:
            if place in seen:
                unique = False
                break
            else:
                seen.append(place)

        if unique == False:
            pos += 1
            seen = []
            continue
        else:
            return window + pos

    return "The condition was never met"

if __name__ == '__main__':
    print(solve(parse("./input"), "one"))
    print(solve(parse("./input"), "two"))