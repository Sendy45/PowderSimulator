from elements import Element
from Grid import Grid

class Stone(Element):
    def __init__(self):
        super().__init__((200, 200, 200))

    def update(self, grid: Grid, x: int, y: int) -> Grid:

        grid.remove_cell(x, y)
        below = grid.get_cell(x, y + 1)

        if not below:
            y += 1

        grid.set_cell(x, y, self)

        return grid