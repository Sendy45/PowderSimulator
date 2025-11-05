import pygame
import config

class Grid:
    def __init__(self, height: int, width: int):
        self.cell_size = 40
        self.height = height // self.cell_size
        self.width = width // self.cell_size
        self.grid: list[list["Element" | None]] = [[None] * width for _ in range(height)]

    def update(self):
        for y in range(self.height, -1, -1): # Bottom left -> upper right
            for x in range(self.width):
                if self.grid[y][x]:
                    self.grid[y][x].update(self, x, y)

    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]:
                    color = self.grid[y][x].color
                    pygame.draw.rect(config.SCREEN, color, pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

    def get_cell(self, x: int, y: int) -> "Element | None":
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self.grid[y][x]

    def set_cell(self, x: int, y: int, element: "Element"):
        if not(x < 0 or x >= self.width or y < 0 or y >= self.height):
            self.grid[y][x] = element

    def clear(self):
        self.grid = [[None] * self.width for _ in range(self.height)]

    def remove_cell(self, x: int, y: int):
        if not (x < 0 or x >= self.width or y < 0 or y >= self.height):
            self.grid[y][x] = None