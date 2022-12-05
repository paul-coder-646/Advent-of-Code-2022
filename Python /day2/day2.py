def parse(textinput):
    with open(textinput, "r") as input:
        lines = input.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].strip().split(" ")
    return lines

def solve(input, part):
    rockopponent = 'A'
    paperopponent = 'B'
    scissorsopponent = 'C'
    rockme = 'X'
    paperme = 'Y'
    scissorsme = 'Z'

    score = 0
    lines = input

    #part1
    if part == "one":

        for i in range(len(lines)):
            win = False
            draw = False

            if lines[i][0] == rockopponent and lines[i][1] == paperme:
                win = True
            elif lines[i][0] == scissorsopponent and lines[i][1] == rockme:
                win = True
            elif lines[i][0] == paperopponent and lines[i][1] == scissorsme:
                win = True

            elif lines[i][0] == scissorsopponent and lines[i][1] == scissorsme:
                draw = True
            elif lines[i][0] == paperopponent and lines[i][1] == paperme:
                draw = True
            elif lines[i][0] == rockopponent and lines[i][1] == rockme:
                draw = True


            lines[i].append(win)
            lines[i].append(draw)

        for i in range(len(lines)):
            # if we won, count that play towards our score
            if lines[i][2] == True:
                if lines[i][1] == rockme:
                    score += 7
                elif lines[i][1] == paperme:
                    score += 8
                elif lines[i][1] == scissorsme:
                    score += 9

            #draw
            elif lines[i][3] == True:
                if lines[i][1] == rockme:
                    score += 4
                elif lines[i][1] == paperme:
                    score += 5
                elif lines[i][1] == scissorsme:
                    score += 6
            #loss
            else:
                if lines[i][1] == rockme:
                    score += 1
                elif lines[i][1] == paperme:
                    score += 2
                elif lines[i][1] == scissorsme:
                    score += 3

    # part2
    elif part == "two":
        loss = "X"
        draw = "Y"
        win = "Z"

        for i in range(len(lines)):
            if lines[i][0] == rockopponent and lines[i][1] == win:
                lines[i][1] = paperme
            elif lines[i][0] == scissorsopponent and lines[i][1] == win:
                lines[i][1] = rockme
            elif lines[i][0] == paperopponent and lines[i][1] == win:
                lines[i][1] = scissorsme

            elif lines[i][0] == rockopponent and lines[i][1] == draw:
                lines[i][1] = rockme
            elif lines[i][0] == scissorsopponent and lines[i][1] == draw:
                lines[i][1] = scissorsme
            elif lines[i][0] == paperopponent and lines[i][1] == draw:
                lines[i][1] = paperme

            elif lines[i][0] == rockopponent and lines[i][1] == loss:
                lines[i][1] = scissorsme
            elif lines[i][0] == scissorsopponent and lines[i][1] == loss:
                lines[i][1] = paperme
            elif lines[i][0] == paperopponent and lines[i][1] == loss:
                lines[i][1] = rockme

        score = solve(lines, "one")

    return score

if __name__ == '__main__':
    print(solve(parse("./input"), "one"))
    print(solve(parse("./input"), "two"))





