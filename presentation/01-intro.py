import itertools as it
from dataclasses import dataclass

from manim import *


@dataclass
class Point:
    """x y coordinate"""

    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return f"[{self.x},{self.y}]"

    def is_neighbor(self, other) -> bool:
        return abs(self.x - other.x) + abs(self.y - other.y) == 1

    def __hash__(self) -> int:
        return hash((self.x, self.y))


def get_graph():
    with open("maps/01.txt", "r") as f:
        m = [[int(c) for c in line if c != "\n"] for line in f.readlines()]
        vertices = [
            Point(x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 0
        ]
        start, end = [
            Point(x, y) for y, row in enumerate(m) for x, v in enumerate(row) if v == 2
        ]

        vertices.append(start)
        vertices.append(end)

        indexed_vertices = dict(enumerate(vertices))
        edges = [
            (a[0], b[0])
            for a, b in it.combinations(indexed_vertices.items(), 2)
            if a[1].is_neighbor(b[1]) == 1
        ]

        return edges, indexed_vertices


class Intro(Scene):
    def construct(self):
        title = Text("What is a graph?", font="Consolas").scale(1.5)
        self.play(Write(title))
        self.wait(1)
        self.play(Unwrite(title))

        edges, vertices = get_graph()
        g = Graph(vertices.keys(), edges)
        self.play(Create(g))

        self.play(
            g[k].animate.move_to([v.x - 4.5, v.y - 4.5, 0]) for k, v in vertices.items()
        )

        self.wait(2)
