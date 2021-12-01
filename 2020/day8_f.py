import time

tick = time.time()

accumulator = 0
order = 0
instructions = []
history = []

with open('./inputs/day8.txt') as ins:
    lines = ins.readlines()

while order < len(lines):
    if order in history:
        break

    splitted_ins = lines[order].split()
    op = splitted_ins[0]
    arg = splitted_ins[1]

    if op == "acc":
        accumulator += int(arg)
    elif op == "jmp":
        order += int(arg)
        if order < 0:
            order == 0
        continue

    history.append(order)
    order += 1

print(accumulator)

tack = time.time()
print(tack-tick)
