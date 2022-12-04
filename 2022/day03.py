from pathlib import Path
from string import ascii_letters


def read_puzzle_input():
    puzzle_input = Path(__file__).parent / f"input/{Path(__file__).stem}.txt"
    return puzzle_input.read_text()


def search_same_character_in_compartments(compartment):
    for part in compartment[0]:
        if part in compartment[1]:
            return part


def split_groups(iterable, chunk_size):
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i:i + chunk_size]


def search_same_character_in_group(group):
    for character in group[0]:
        if character in group[1] and character in group[2]:
            return character

    return None


def main():
    priorities = {letter: index + 1 for index, letter in enumerate(ascii_letters)}
    rucksacks = [line for line in read_puzzle_input().splitlines()]

    rucksack_compartments = [[c[slice(0, len(c) // 2)], c[slice(len(c) // 2, len(c))]] for c in rucksacks]

    # Part 1
    sum_of_priorities = 0
    for compartments in rucksack_compartments:
        sum_of_priorities += priorities[search_same_character_in_compartments(compartments)]
    print("Part 1:", sum_of_priorities)

    # Part 2
    sum_of_group_priorities = 0
    groups = list(split_groups(rucksacks, 3))
    for group in groups:
        sum_of_group_priorities += priorities[search_same_character_in_group(group)]
    print("Part 2:", sum_of_group_priorities)


if __name__ == '__main__':
    main()
