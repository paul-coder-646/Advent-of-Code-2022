def parse(input):
    with open(input, "r") as input:
        lines = input.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n").split(" ")
        if len(lines[i]) > 1:
            lines[i][1] = int(lines[i][1])
        else:
            lines[i].append(" ")
    return lines

def solve(input, part):
    cycle = 0
    cycles = []
    register = 1
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    for instruc in range(len(input)):
        if input[instruc][0] == "noop":
            cycle += 1
            if cycle in interesting_cycles:
                cycles.append(cycle * register)

        if input[instruc][0] == "addx":
            for _ in range(2):
                cycle += 1
                if cycle in interesting_cycles:
                    cycles.append(cycle * register)
            register += input[instruc][1]
    return sum(cycles)

if __name__ == '__main__':
    print(solve(parse("./input"), "One"))