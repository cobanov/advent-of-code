with open("./inputs/day1.txt") as file:
    data = [int(line.strip()) for line in file]


# Part 1
counter = 0

for index, value in enumerate(data[:-1]):
    if data[index+1] > value:
        counter += 1

print(counter)

# Part 2

window_size = 3
counter_2 = 0
for index, value in enumerate(data):
    if sum(data[index: index+window_size]) < sum(data[index+1:index+window_size+1]):
        counter_2 += 1

print(counter_2)
