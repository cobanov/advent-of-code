with open('./day8.txt') as file:
    data = [(line.strip().split(' ')) for line in file]


location = 0
accumulator = 0
past_locations = []
command, value = data[location]

while True:
    past_locations.append(location)
    command, value = data[location]
    before_location = location

    if command == 'jmp':
        location += int(value)

    if command == 'acc':
        accumulator += int(value)
        location += 1

    if command == 'nop':
        location += 1

    if location in past_locations:
        print('Accumulator: ', accumulator)
        break
