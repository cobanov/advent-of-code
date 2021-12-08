import dataclasses


with open('./inputs/day8.txt') as file:
    data = [i.split('|') for i in file.read().split('\n')]


digits = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for x, y in data:
    for output in y.strip().split(' '):
        if len(output) == 2:
            digits[1] += 1

        elif len(output) == 4:
            digits[4] += 1

        elif len(output) == 3:
            digits[7] += 1

        elif len(output) == 7:
            digits[8] += 1


print(digits)
print(sum([i for i in digits.values()]))
