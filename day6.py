import collections
with open("day6.txt") as file:
    data = file.read()
    groups = data.split('\n\n')

# Problem 1
group_concat = [''.join(i.replace('\n', '')) for i in groups]

counter = 0
for answers in group_concat:
    counter += len(set(answers))

print('Answer 1: ', counter)

# Problem 2 - Needs update

part2 = sum(len(set.intersection(*map(set, group))) for group in groups)
print(part2)
