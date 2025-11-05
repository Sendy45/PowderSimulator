from elements import Element
from Grid import Grid
from random import choice

class Water(Element):
    def __init__(self):
        super().__init__((0, 0, 255))
        self.direction = 1

    def update(self, grid: Grid, x: int, y: int) -> Grid:

        self.direction = choice([-1, 1])
        grid.remove_cell(x, y)
        below = grid.get_cell(x, y + 1)
        next_cell = grid.get_cell(x + self.direction, y)
        next_below = grid.get_cell(x + self.direction, y + 1)

        if not below:
            y += 1
        elif not next_below and not next_cell:
            y += 1
            x += self.direction
        elif not next_cell:
            x += self.direction

        grid.set_cell(x, y, self)

        return grid