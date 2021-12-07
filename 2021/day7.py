import numpy as np

with open('./inputs/day7.txt') as file:
    numbers = [int(i) for i in file.read().split(',')]

# Part 1
steps = numbers - np.median(numbers)
print('Answer 1: ', sum(abs(steps)))

# Part 2
steps = abs(numbers - np.round(np.mean(numbers))-1)
sum_list = [sum(i) for i in [range(int(i+1)) for i in steps]]
print('Answer 2: ', sum(sum_list))
