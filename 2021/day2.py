with open("./inputs/day2.txt") as file:
    data = [line.strip().split(' ') for line in file]


horizontal, depth = 0, 0


for command, value in data:

    if command == 'forward':
        horizontal += int(value)

    elif command == 'down':
        depth += int(value)

    elif command == 'up':
        depth -= int(value)

print('Answer 1: ', (horizontal * depth))


# Part 2

horizontal, depth = 0, 0
aim = 0

for command, value in data:

    if command == 'forward':
        horizontal += int(value)
        depth += int(value) * aim

    elif command == 'down':
        aim += int(value)

    elif command == 'up':
        aim -= int(value)

print('Answer 2: ', (horizontal * depth))
