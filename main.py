import pygame
import os
import random

pygame.init()

SCR_H = 700
SCR_W = 1100
SCREEN = pygame.display.set_mode((SCR_W,SCR_H))

# Замените эти пути на реальные пути к вашим изображениям
RUNNING = [pygame.image.load(os.path.join("demon", "demonrun1.png")),
           pygame.image.load(os.path.join("demon", "demonrun2.png")),
           pygame.image.load(os.path.join("demon", "demonrun3.png")),
           pygame.image.load(os.path.join("demon", "demonrun4.png"))]

class Demon:
    X_POS = 80
    Y_POS = 400

    def __init__(self):
        self.run_img = RUNNING
        self.demon_run = True
        self.step_index = 0
        self.image = self.run_img[0]
        self.demon_rect = self.image.get_rect()
        self.demon_rect.x = self.X_POS
        self.demon_rect.y = self.Y_POS

    def update(self, userInput):
        if self.demon_run:
            self.run()
        if self.step_index >= 10:
            self.step_index = 0
    
    def run(self):
        self.image = self.run_img[self.step_index // 4]
        self.demon_rect = self.image.get_rect()  # Исправлено на demon_rect
        self.demon_rect.x = self.X_POS
        self.demon_rect.y = self.Y_POS
        self.step_index += 1

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.demon_rect.x, self.demon_rect.y))  # Исправлено на demon_rect

def main():
    global points
    points = 0
    run = True
    clock = pygame.time.Clock()  # Добавлен clock для контроля FPS
    player = Demon()
    
    while run:
        # Один обработчик событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)
        
        pygame.display.update()
        clock.tick(30)  # Ограничение FPS
        
    pygame.quit()

if __name__ == "__main__":
    main()