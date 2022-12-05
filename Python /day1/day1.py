def solve(path, part):
    elve = 0
    elves = []

    with open(path, "r") as input:
        lines = input.readlines()

        for i, line in enumerate(lines):
            line = line.strip("\n")
            if line != '':
                elve += int(line)
            if line == '':
                elves.append(elve)
                elve = 0
                continue

    if part == "one":
        return sorted(elves, reverse=True)[0]
    else:
        return sum(sorted(elves, reverse=True)[0:3])

if __name__ == '__main__':
    print(solve("./input", "two"))