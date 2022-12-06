from pathlib import Path


def read_puzzle_input():
    puzzle_input = Path(__file__).parent / f"input/{Path(__file__).stem}.txt"
    return puzzle_input.read_text()


def find_marker(datastream, length_of_marker):
    marker = []
    for i, c in enumerate(datastream):
        if len(marker) < length_of_marker:
            marker.append(c)
        else:
            marker = marker[1:]
            marker.append(c)
        if len(set(marker)) == length_of_marker:
            return i + 1, marker
    return None


def main():
    print(read_puzzle_input())

    # Part 1
    print(f"Part 1: {find_marker(read_puzzle_input(), 4)}")

    # Part 2
    print(f"Part 2: {find_marker(read_puzzle_input(), 14)}")


if __name__ == '__main__':
    main()
