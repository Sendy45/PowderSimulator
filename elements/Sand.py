from elements import Element
from Grid import Grid

class Sand(Element):
    def __init__(self):
        super().__init__((100, 30, 0))

    def update(self, grid: Grid, x: int, y: int) -> Grid:

        grid.remove_cell(x, y)
        below = grid.get_cell(x, y + 1)
        below_left = grid.get_cell(x - 1, y + 1)
        below_right = grid.get_cell(x + 1, y + 1)
        left = grid.get_cell(x - 1, y)
        right = grid.get_cell(x + 1, y)

        if not below:
            y += 1
        elif not below_left and not left:
            y += 1
            x -= 1
        elif not below_right and not right:
            y += 1
            x += 1

        grid.set_cell(x, y, self)

        return grid