#usr/local/bin/python3

input = open('input').read()

elves = [[int(num) for num in elf.splitlines()] for elf in input.split('\n\n')]
elves = sorted([sum(elf) for elf in elves])
top_three = elves[-3:]
top_elf = elves[-1]
