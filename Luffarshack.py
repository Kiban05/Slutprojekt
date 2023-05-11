import pygame
import numpy as np
import os

SIZE = 600
ROWS = 20
WIN = pygame.display.set_mode((SIZE, SIZE))
SpaceBtwRows = SIZE // ROWS
FPS = 60 
CROSS_IMAGE = pygame.image.load(os.path.join('cross.png'))
CROSS_IMAGE = pygame.transform.scale(CROSS_IMAGE, (24, 24))

cells = np.zeros((ROWS,ROWS), dtype=int)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def grid(WIN, SIZE, ROWS):
    x = 0 
    y = 0
    for l in range(ROWS):
        x += SpaceBtwRows
        y += SpaceBtwRows
        pygame.draw.line(WIN, (BLACK), (x, 0), (x, SIZE))

        pygame.draw.line(WIN, (BLACK), (0, y), (SIZE, y))

def draw_window():
    WIN.fill(WHITE)
    grid(WIN, SIZE, ROWS)
    for row in range(ROWS):
        for column in range(ROWS):
            if cells[row, column] == 1:
                x = row * SpaceBtwRows
                y = column * SpaceBtwRows
                #pygame.draw.circle(WIN, (BLACK), (x + 15, y + 15), 12)
                WIN.blit(CROSS_IMAGE, (x + 3, y + 3))
    
    pygame.display.update()

    
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, column = pos[0] // SpaceBtwRows, pos[1] // SpaceBtwRows
                cells[row, column] = 1
                
                        
        draw_window()
        

    pygame.quit()

if __name__ == "__main__":
    main()