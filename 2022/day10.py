from utils.Import import read_puzzle_input


class VideoDevice:
    class CRT:
        def __init__(self):
            self.display = [["."] * 40 for _ in range(6)]  # `for` syntax to avoid referencing the same item

        def print_display(self):
            for row in self.display:
                print(*row, sep='')

        def update_display(self, x, cycle):
            row = (cycle - 1) // 40
            pos = (cycle - 1) % 40
            # print(f"Cycle: {cycle}, Current Position: {row, pos}, Sprite Position: {x - 1, x, x + 1}")

            if pos in [x - 1, x, x + 1]:
                self.display[row][pos] = '#'

    class CPU:
        def __init__(self, crt):
            self.x = 1
            self.cycle = 0
            self.signal_strength_marker = [20, 60, 100, 140, 180, 220]
            self.signal_strength = 0
            self.crt = crt

        def perform(self, operation: str):
            if operation == 'noop':
                self.increment_cycle()
            elif operation.startswith('addx'):
                self.increment_cycle()
                self.increment_cycle()
                self.x += int(operation.split()[-1])

        def increment_cycle(self):
            self.cycle += 1
            self.check_signal_strength()
            self.crt.update_display(self.x, self.cycle)

        def check_signal_strength(self):
            if self.cycle in self.signal_strength_marker:
                self.signal_strength += self.x * self.cycle

    def __init__(self):
        self.crt = self.CRT()
        self.cpu = self.CPU(self.crt)


def main():
    operations = read_puzzle_input(__file__).splitlines()

    vd = VideoDevice()

    for operation in operations:
        vd.cpu.perform(operation=operation)

    print(f"Part 1: {vd.cpu.signal_strength}")

    print("Part 2:")
    vd.crt.print_display()


if __name__ == '__main__':
    main()
