from pathlib import Path


def read_puzzle_input(file):
    puzzle_input = Path(file).parent / f"input/{Path(file).stem}.txt"
    return puzzle_input.read_text()
