def parse(textinput):
    with open(textinput, "r") as input:
        lines = input.readlines()

        for i in range(len(lines)):
            lines[i] = [*lines[i].strip()]
    return lines

def solve(input, part):
    result = 0
    duplicates = []
    seen = []
    if part == "one":
        for i in range(len(input)):
            seen = []
            for j in range(len(input[i])//2):
                seen.append(input[i][j])
            for k in range(len(input[i])//2, len(input[i])):
                if input[i][k] in seen:
                    duplicates.append(input[i][k])
                    break

    if part == "two":
        for i in range(len(input)//3):
            preduplicates = []

            for second in input[3*i+1]:
                if second in input[3*i]:
                    preduplicates.append(second)

            for third in input[3*i+2]:
                if third in preduplicates:
                    duplicates.append(third)
                    break

    for character in duplicates:
        if (ord(character) < 97):
            result += ord(character) - 65 + 27
        else:
            result += (ord(character) - 96)

    return len(duplicates), result

if __name__ == '__main__':
    print(solve(parse("./input"), "one"))
    print(solve(parse("./input"), "two"))
