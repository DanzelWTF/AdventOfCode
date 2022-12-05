from pathlib import Path


def read_puzzle_input():
    puzzle_input = Path(__file__).parent / f"input/{Path(__file__).stem}.txt"
    return puzzle_input.read_text()


def prepare_pairs(pairs):
    pairs = [pair.split(",") for pair in pairs]
    for pair in pairs:
        pair[0] = list(map(int, pair[0].split("-")))
        pair[1] = list(map(int, pair[1].split("-")))
    return pairs


def main():
    pairs = [line for line in read_puzzle_input().splitlines()]
    pairs = prepare_pairs(pairs)

    # Part 1
    count_fully_containing_pairs = 0
    for pair in pairs:
        if (set(range(pair[0][0], pair[0][1] + 1)).issubset(set(range(pair[1][0], pair[1][1] + 1)))) or (
                set(range(pair[1][0], pair[1][1] + 1)).issubset(set(range(pair[0][0], pair[0][1] + 1)))):
            count_fully_containing_pairs += 1
    print("Part 1:", count_fully_containing_pairs)

    # Part 2
    count_overlapping_pairs = 0
    for pair in pairs:
        if set(range(pair[0][0], pair[0][1] + 1)).intersection(set(range(pair[1][0], pair[1][1] + 1))):
            count_overlapping_pairs += 1
    print("Part 2:", count_overlapping_pairs)


if __name__ == '__main__':
    main()
