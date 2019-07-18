import pygame

class Snake:
    def __init__(self):

        self.head =[45,45]

    def moove(self,control):
        """движение змеи в зависимости от направлеия"""
        if control.flag_direction == "RIGHT":
            self.head[0] += 25
        elif control.flag_direction == "LEFT":
            self.head[0] -= 25
        elif control.flag_direction == "UP":
            self.head[1] -= 25
        elif control.flag_direction == "DOWN":
            self.head[1] += 25

    def draw_snake(self,window):
        """Отрисовка змеи на экране"""
        pygame.draw.rect(window,pygame.Color("Green"),pygame.Rect(self.head[0],self.head [1],10,10))