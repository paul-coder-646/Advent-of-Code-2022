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
            seen = []
            preduplicates = []

            one = input[3*i]
            two = input[3*i+1]
            three = input[3*i+2]

            for onechar in one:
                seen.append(onechar)
            for twochar in two:
                if twochar in seen:
                    preduplicates.append(twochar)
            for threechar in three:
                if threechar in preduplicates:
                    duplicates.append(threechar)
                    break


    for character in duplicates:
        if (ord(character) < 97):
            result += ord(character) - 65 + 27
        else:
            result += (ord(character) - 96)

    return len(duplicates), result

if __name__ == '__main__':
    print(solve(parse("./input"), "two"))
