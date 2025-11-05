from __future__ import annotations
from Grid import Grid
class Element:
    def __init__(self, color: tuple[int, int, int]):
        self.color = color

    def update(self, grid: Grid, x: int, y: int):
        pass