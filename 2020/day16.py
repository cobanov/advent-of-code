

with open('./inputs/day16.txt') as file:

    document = [line.strip() for line in file]
    # Rules
    rules = document[:20]
    rules = [line.split(':')[1] for line in rules]
    rules = [line.strip().split('or') for line in rules]
    rules = [val.strip() for sublist in rules for val in sublist]

    # Nearby tickets
    nearby = document[25:]

# Calculate Space

space = []

for interval in rules:
    min, max = interval.split('-')
    space.extend(range(int(min), int(max)))
space = set(space)

####


# # Nearby Tickets
error_rate = 0

for ticket in nearby:
    numbers = ticket.split(',')
    integer_list = list(map(int, numbers))
    for number in integer_list:
        if number not in space:
            error_rate += number
            print('Invalid', number)

print(error_rate)
