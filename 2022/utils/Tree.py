class Node:
    def __init__(self, name, parent=None, size=0):
        self.name: str = name
        self.children: list[Node] = []
        self.parent: Node = parent
        self.size: int = size

    def __str__(self):
        if self.children:
            return f"- {self.name} (dir, size: {self.size})"
        else:
            return f"- {self.name} (file, size: {self.size})"

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        return self.size > other

    def __ge__(self, other):
        return self.size >= other

    def __lt__(self, other):
        return self.size < other

    def __le__(self, other: int):
        return self.size <= other

    def __radd__(self, other):
        return self.size + other


class Tree:
    def __init__(self):
        self.root: Node = Node('/')
        self.pwd: Node = self.root
        self.dirs: list[Node] = []

    def add_node(self, name: str, size: int = 0):
        new_node = Node(name, self.pwd, size)
        self.pwd.children.append(new_node)
        if size == 0:  # if directory
            self.dirs.append(new_node)  # add to dirs list
            self.pwd = new_node  # update current directory

    def go_up(self):
        self.pwd = self.pwd.parent

    def print_tree(self, node: Node, level: int = 0):
        print(f"{'  ' * level}{node}")
        for child in node.children:
            self.print_tree(child, level + 1)

    def update_sizes(self):
        for child in self.root.children:
            self.root.size += self.update_size_childrens(child)

    def update_size_childrens(self, node):
        for child in node.children:
            node.size += self.update_size_childrens(child)
        return node.size
