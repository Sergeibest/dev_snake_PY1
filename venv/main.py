import pygame
from control import Control
from snake import Snake

pygame.init()
window = pygame.display.set_mode((441,441))
pygame.display.set_caption("Змейка")
control = Control()
snake = Snake()
var_speed = 0

while control.flag_game:
    control.control()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag_game = False
    window.fill(pygame.Color("Black"))
    snake.draw_snake(window)
    if var_speed % 1000 == 0:
        snake.moove(control)
    var_speed += 1
    pygame.display.flip()
    ''''тест-эту дичь надо убрать'''
