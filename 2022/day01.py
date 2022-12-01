import os


def read_puzzle_input():
    with open("input/day01.txt") as f:
        return f.read()


def day01():
    elf_calories = [[int(x) for x in elf.split(os.linesep) if x != ''] for elf in
                    read_puzzle_input().split(os.linesep + os.linesep)]
    elf_calories_sum = [sum(elf) for elf in elf_calories]
    print(f"Part 1: {max(elf_calories_sum)}")

    elf_calories_sum.sort(reverse=True)
    print(f"Part 2: {sum(elf_calories_sum[:3])}")


if __name__ == "__main__":
    day01()
