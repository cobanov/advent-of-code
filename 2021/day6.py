from collections import Counter
with open('./inputs/test.txt') as file:
    fishes = [int(i) for i in file.read().split(',')]

# for iteration in range(21):
#     for index, value in enumerate(fishes):
#         fishes[index] -= 1
#         if fishes[index] == -1:
#             fishes.append(9)
#             fishes[index] = 6

#     print('I:', iteration+1, 'C:', len(fishes), fishes)


fish_population = Counter(fishes)
day = 26
for i in range(day):
    print(i)
