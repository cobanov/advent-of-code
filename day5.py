with open("./inputs/day5.txt") as file:
    data = [line.strip() for line in file]

binarized = [board.replace('F', '0').replace('B', '1').replace(
    'R', '1').replace('L', '0') for board in data]

# Part 1
calculated = set([int(ticket, 2) for ticket in binarized])
print('Answer 1: ', max(calculated))

# Part 2
possible_tickets = set(range(min(calculated), max(calculated)))
differences = possible_tickets - calculated
print('Answer 2: ', differences)
