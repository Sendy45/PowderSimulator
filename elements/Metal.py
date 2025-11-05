from elements import Element
from Grid import Grid

class Metal(Element):
    def __init__(self):
        super().__init__((50, 50, 50))

    def update(self, grid: Grid, x: int, y: int) -> Grid:

        return grid