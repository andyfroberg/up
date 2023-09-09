import pygame
import sys


class Controller:
    def __init__(self, model, view):
        pygame.init()
        self.model = model
        self.view = view
        self.running = True

    def register_view(self, view):
        self.view = view

    def start(self):
        while self.running:
            # 1) Get input from the user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            keys = pygame.key.get_pressed()

            





if __name__ == "__main__":
    pass