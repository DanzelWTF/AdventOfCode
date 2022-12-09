import re
import copy
from pathlib import Path


def read_puzzle_input():
    puzzle_input = Path(__file__).parent / f"input/{Path(__file__).stem}.txt"
    return puzzle_input.read_text()


def prepare_cargo(cargo_lines):
    cargo = {}
    cargo_regex = re.compile(r'[A-Z]')

    # find cargo
    for _, line in enumerate(cargo_lines):
        for m in cargo_regex.finditer(line):
            cargo.setdefault(m.start() // 4 + 1, []).append(m.group(0))

    # sort cargo stacks and reverse items
    cargo = dict(sorted({k: v[::-1] for k, v in cargo.items()}.items()))

    return cargo


def move_with_crate_mover_9000(cargo, operations):
    for operation in operations:
        operation = operation.split()
        number_of_crates, from_stack, to_stack = map(int, [operation[1], operation[3], operation[5]])
        for _ in range(number_of_crates):
            cargo[to_stack].append(cargo[from_stack].pop())
    return cargo


def move_with_crate_mover_9001(cargo, operations):
    for operation in operations:
        operation = operation.split()
        number_of_crates, from_stack, to_stack = map(int, [operation[1], operation[3], operation[5]])

        cargo[to_stack].extend(cargo[from_stack][-number_of_crates:])
        cargo[from_stack] = cargo[from_stack][:-number_of_crates]

    return cargo


def main():
    cargo = prepare_cargo(read_puzzle_input().splitlines()[:8])
    operations = read_puzzle_input().splitlines()[10:]

    # Part 1
    cargo_part_1 = move_with_crate_mover_9000(copy.deepcopy(cargo), operations)
    last_crates = []
    for carte in cargo_part_1.values():
        last_crates.append(carte[-1])
    print(f"Part 1: {''.join(last_crates)}")


    # Part 2
    cargo_part_2 = move_with_crate_mover_9001(copy.deepcopy(cargo), operations)
    last_crates = []
    for carte in cargo_part_2.values():
        last_crates.append(carte[-1])
    print(f"Part 2: {''.join(last_crates)}")


if __name__ == '__main__':
    main()
