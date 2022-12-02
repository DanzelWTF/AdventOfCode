from pathlib import Path


def read_puzzle_input():
    puzzle_input = Path(__file__).parent / f"input/{Path(__file__).stem}.txt"
    return puzzle_input.read_text()


def part1_get_points_for_shape(shape):
    # X = Rock (1p), Y = Paper (2p), Z = Scissors (3p)
    points = {'X': 1, 'Y': 2, 'Z': 3}
    return points[shape]


def part1_get_points_for_round(s1, s2):
    # Win = 6p, Draw = 3p, Loss = 0p
    # Draw: X = A, Y = B, Z = C
    # Win: X beats C, Y beats A, Z beats B
    points = 0
    if (s1 == "A" and s2 == "X") or (s1 == "B" and s2 == "Y") or (s1 == "C" and s2 == "Z"):
        points += 3
    elif (s1 == "A" and s2 == "Y") or (s1 == "B" and s2 == "Z") or (s1 == "C" and s2 == "X"):
        points += 6
    return points


def part2_get_points_for_shape(player1, outcome):
    # X = Rock (1p), Y = Paper (2p), Z = Scissors (3p)
    points = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    if outcome == 'X':  # Loss
        if player1 == 'A':  # Rock beats Scissors
            return points['Scissors']
        elif player1 == 'B':  # Paper beats Rock
            return points['Rock']
        elif player1 == 'C':  # Scissors beats Paper
            return points['Paper']
    elif outcome == 'Y':  # Draw
        if player1 == 'A':  # Rock
            return points['Rock']
        elif player1 == 'B':  # Paper
            return points['Paper']
        elif player1 == 'C':  # Scissors
            return points['Scissors']
    elif outcome == 'Z':  # Win
        if player1 == 'A':  # Paper beats Rock
            return points['Paper']
        elif player1 == 'B':  # Scissors beats Paper
            return points['Scissors']
        elif player1 == 'C':  # Rock beats Scissors
            return points['Rock']


def part2_get_points_for_round(outcome):
    points = {'X': 0, 'Y': 3, 'Z': 6}
    return points[outcome]


def main():
    games = [line for line in read_puzzle_input().splitlines()]

    part1_points = 0
    for game in games:
        part1_points += part1_get_points_for_shape(game[2])
        part1_points += part1_get_points_for_round(game[0], game[2])
    print(f"Part 1: {part1_points}")

    part2_points = 0
    for game in games:
        part2_points += part2_get_points_for_shape(game[0], game[2])
        part2_points += part2_get_points_for_round(game[2])
    print(f"Part 2: {part2_points}")


if __name__ == "__main__":
    main()
