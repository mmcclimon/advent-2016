import collections
from dataclasses import dataclass
import itertools
import math
from typing import Set, Tuple


def main():
    sample = State(0, 0, ({"HM", "LM"}, {"HG"}, {"LG"}, set()))
    _ = sample

    part1 = State(
        0,
        0,
        (
            {"PmG", "PmM"},
            {"CoG", "CmG", "RuG", "PuG"},
            {"CoM", "CmM", "RuM", "PuM"},
            set(),
        ),
    )

    part2 = part1.clone()
    part2.floors[0].update(["ElG", "ElM", "DlG", "DlM"])

    find_best(part2)
    # find_best(part2)


def find_best(start):
    best = math.inf
    todo = collections.deque([start])
    seen = set()

    ohno = 0

    while todo:
        ohno = max(ohno, len(todo))
        state = todo.popleft()

        if state.is_done():
            print(f"DONE: {state}")
            best = min(best, state.steps)

        if state.steps > best:
            continue

        for candidate in state.next():
            k = candidate.key()
            if k not in seen:
                seen.add(k)
                todo.append(candidate)

    print(f"best: {best} ({ohno=})")


@dataclass
class State:
    elevator: int
    steps: int
    floors: Tuple[Set[str], Set[str], Set[str], Set[str]]

    def __repr__(self):
        floors = ", ".join(f"{i+1}={self.floors[i]}" for i in range(4))
        return f"<State n={self.steps}, E={self.elevator+1}, {floors}>"

    def key(self):
        f = self.floors
        return (
            self.elevator,
            tuple(sorted(f[0])),
            tuple(sorted(f[1])),
            tuple(sorted(f[2])),
            tuple(sorted(f[3])),
        )

    def next(self):
        floor = self.floors[self.elevator]
        others = [f for f in range(4) if abs(f - self.elevator) == 1]
        ret = []

        for n_objs in [1, 2]:
            for contents in itertools.combinations(floor, n_objs):
                for f in others:
                    ret.append(self.move(contents, f))

        return [s for s in ret if s.is_valid()]

    def is_valid(self):
        # print(self)
        for f in range(4):
            floor = self.floors[f]
            chips = {obj.removesuffix("M") for obj in floor if obj.endswith("M")}
            gens = {obj.removesuffix("G") for obj in floor if obj.endswith("G")}

            # invalid if there are chips not attached to their generators
            if gens and chips - gens:
                return False

        return True

    def clone(self):
        return self.__class__(
            self.elevator,
            self.steps,
            (
                self.floors[0].copy(),
                self.floors[1].copy(),
                self.floors[2].copy(),
                self.floors[3].copy(),
            ),
        )

    def move(self, els, floor):
        new = self.clone()
        new.elevator = floor
        new.steps += 1

        locs = {el: f for el in els for f in range(4) if el in self.floors[f]}

        for el, loc in locs.items():
            new.floors[loc].remove(el)
            new.floors[floor].add(el)

        return new

    def is_done(self):
        f = self.floors
        return len(f[0]) == 0 and len(f[1]) == 0 and len(f[2]) == 0


if __name__ == "__main__":
    main()
