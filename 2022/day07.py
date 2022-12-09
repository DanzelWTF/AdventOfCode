from utils.Tree import Tree
from utils.Import import read_puzzle_input


def main():
    # Prepare data
    operations = read_puzzle_input(__file__).splitlines()

    file_structure = Tree()

    for operation in operations[1:]:
        if operation.startswith("$ cd .."):  # cd ..
            file_structure.go_up()
        elif operation.startswith("$ cd"):  # directory
            file_structure.add_node(operation.split(" ")[-1])
        elif operation[0].isdigit():        # file
            file_structure.add_node(operation.split(" ")[-1], int(operation.split(" ")[0]))

    file_structure.update_sizes()

    # Part 1
    print(f"Part 1: {sum(filter(lambda x: x.size <= 100000, file_structure.dirs))}")

    # Part 2
    unused_space = 70000000-file_structure.root.size
    additional_space_required = 30000000-unused_space
    suitable_dirs = list(filter(lambda x: x.size >= additional_space_required, file_structure.dirs))
    suitable_dirs.sort()
    print(f"Part 2: {suitable_dirs[0].size}")


if __name__ == '__main__':
    main()
