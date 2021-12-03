import collections

with open("./inputs/day3.txt") as file:
    data = [line.strip() for line in file]


bits = collections.defaultdict(list)

for i in range(12):
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

print(most_int * least_int)
