import collections

with open("./inputs/day3.txt") as file:
    data = [line.strip() for line in file]

bits = collections.defaultdict(list)

for i in range(len(data[0])):
    for number in data:
        bits[i].append(number[i])


most_bits = []
least_bits = []
for key, value in bits.items():
    occurence_count = collections.Counter(value)
    most_bits.append(occurence_count.most_common(1)[0][0])
    least_bits.append(occurence_count.most_common()[-1][0][0])

most_int = int(''.join(most_bits), 2)
least_int = int(''.join(least_bits), 2)

print('Answer 1: ', most_int * least_int)


# Part 2
oxygen = data
oxygen_rating = 0

for i in range(len(data[0])):
    bit_counter = {'0': 0, '1': 0}

    for number in oxygen:
        bit_counter[number[i]] += 1

    if bit_counter['1'] >= bit_counter['0']:
        most_common = '1'

    else:
        most_common = '0'

    oxygen = [n for n in oxygen if n[i] == most_common]

    if len(oxygen) == 1:
        oxygen_rating = int(oxygen[0], 2)

co2 = data
co2_rating = 0

for i in range(len(data[0])):
    bit_counter = {'0': 0, '1': 0}

    for number in co2:
        bit_counter[number[i]] += 1

    if bit_counter['1'] < bit_counter['0']:
        least_common = '1'

    else:
        least_common = '0'

    co2 = [n for n in co2 if n[i] == least_common]

    if len(co2) == 1:
        co2_rating = int(co2[0], 2)


print('Answer 2: ', co2_rating * oxygen_rating)
