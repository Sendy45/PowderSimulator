import pygame

import config
from elements import *
from Grid import Grid

clock = pygame.time.Clock()
FPS = 60
delete = False
grid = Grid(config.SCREEN_HEIGHT, config.SCREEN_WIDTH)
current_element = Sand()
def event_handler():
    global current_element, delete
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_element = Sand()
            if event.key == pygame.K_2:
                current_element = Metal()
            if event.key == pygame.K_3:
                current_element = Water()
            if event.key == pygame.K_4:
                current_element = Stone()
            if event.key == pygame.K_d:
                delete = not delete
                print(delete)


pygame.init()

while config.RUNNING:
    config.SCREEN.fill((0, 0, 0))

    event_handler()

    # Handle mouse hold
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # left button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid_x = mouse_x // grid.cell_size
        grid_y = mouse_y // grid.cell_size
        if not grid.get_cell(grid_x, grid_y):
            grid.set_cell(grid_x, grid_y, current_element)
        if delete:
            grid.remove_cell(grid_x, grid_y)

    grid.draw()
    grid.update()

    pygame.display.flip()

    clock.tick(20)

pygame.quit()