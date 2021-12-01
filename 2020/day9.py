import itertools

with open('./inputs/day9.txt') as file:
    data = [int(line.strip()) for line in file]


def solution1():
    location = 0
    window_size = 25

    for _ in range(len(data) - window_size):
        window = location + window_size
        numbers = data[location:window]
        comb = [sum(i) for i in itertools.combinations(numbers, 2)]

        if data[window] in comb:
            pass

        else:
            print('NOT Found!')
            print('Answer 1: ', data[window])
            break

        location += 1
    return data[window]


def solution2(answer):

    for location in range(len(data)):
        value = 0
        window_size = 2

        while value < answer:
            window = location + window_size
            numbers = data[location:window]
            value = sum(numbers)
            window_size += 1

        if value == answer:
            print('Answer 2: ', min(numbers) + max(numbers))
            print('Window size: ', window_size)
            print('Location: ', location)

            break


answer1 = solution1()
solution2(answer1)
