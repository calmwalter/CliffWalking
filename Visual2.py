import pygame
import sys
import random


class GAME:
    def __init__(self, row, column, route):
        pygame.init()
        self.row = row
        self.column = column
        self.screen = pygame.display.set_mode((column*50, row*50))
        self.route = route
        pygame.display.update()

    def run(self):
        self.screen.fill((0, 0, 0))
        for i in range(self.row):
            pygame.draw.line(self.screen, (255, 255, 255), [
                                0, i*50], [self.column*50, i*50], 5)
        for i in range(self.column):
            pygame.draw.line(self.screen, (255, 255, 255), [
                                i*50, 0], [i*50, self.row*50], 5)
        pygame.draw.rect(self.screen, (0, 255, 0), [0, 0, 50, 50])
        pygame.draw.rect(self.screen, (0, 0, 255), [
                            self.column*50-50, 0, self.column*50-50, 50])
        pygame.draw.rect(self.screen, (255, 0, 0), [
                            50, 0, self.column*50-100, 50])
        for el in self.route:
            pygame.draw.rect(self.screen, (255, 255, 0), [
                                50*el[1], 50*el[0], 50, 50])
        pygame.display.update()
    def updates(self,route):
        self.route = route
        self.run()

#newGame = GAME(10, 20)
# newGame.run()
