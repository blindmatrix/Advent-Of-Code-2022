import itertools as it

elfs = sorted([sum(map(int, list(group))) for key, group in it.groupby(map(lambda x: x.strip(), open("input.txt", "rt")), lambda x: x == '') if not key], reverse=True)
print("Task 1: %d" % elfs[0])
print("Task 2: %d" % sum(elfs[0:3]))
