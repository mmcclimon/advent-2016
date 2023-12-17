def main():
    n = 3005290
    print("part 1:", Ring(n).go())


class Node:
    def __init__(self, n):
        self.id = n
        self.next: Node | None = None
        # self.prev: Node | None = None


class Ring:
    def __init__(self, n):
        self.n = n
        self.root = Node(1)

        prev = self.root
        for elf in range(2, n + 1):
            node = Node(elf)
            prev.next = node
            prev = node

        prev.next = self.root

    def go(self):
        cur = self.root

        while True:
            if cur == cur.next:
                break

            to_steal = cur.next
            cur.next = to_steal.next
            cur = cur.next

        return cur.id


if __name__ == "__main__":
    main()
