with open('./inputs/day6.txt') as file:
    fishes = [int(i) for i in file.read().split(',')]

for _ in range(18):
    for index, value in enumerate(fishes):
        fishes[index] -= 1
        if fishes[index] == -1:
            fishes.append(9)
            fishes[index] = 6

print('Iteration:', len(fishes))
