import pygame
import numpy as np
import os

SIZE = 600
ROWS = 20
WIN = pygame.display.set_mode((SIZE, SIZE))
SpaceBtwRows = SIZE // ROWS
FPS = 60 

#Importera kryss och ändra storleken
CROSS_IMAGE = pygame.image.load(os.path.join('cross.png'))
CROSS_IMAGE = pygame.transform.scale(CROSS_IMAGE, (24, 24))

#Använder np.zeros för att göra en 20 * 20 array fyld med nollor
cells = np.zeros((ROWS,ROWS), dtype=int)

#färger för trevlighetens skull
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Medod för att rita upp ett 20 * 20 grid
def grid(WIN, SIZE, ROWS):
    WIN.fill(WHITE)
    x = 0 
    y = 0
    for l in range(ROWS):
        x += SpaceBtwRows
        y += SpaceBtwRows
        pygame.draw.line(WIN, (BLACK), (x, 0), (x, SIZE))

        pygame.draw.line(WIN, (BLACK), (0, y), (SIZE, y))
    pygame.display.update()

def draw_window(row, column, marker):

    x = row * SpaceBtwRows
    y = column * SpaceBtwRows
    if marker == "O":
        pygame.draw.circle(WIN, (BLACK), (x + 15, y + 15,), 12)
    else:
        WIN.blit(CROSS_IMAGE, (x + 3, y + 3))
    pygame.display.update()

    
def main():
    global i
    clock = pygame.time.Clock()
    run = True
    i = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if i % 2 == 0:
                    marker = "X"
                    q = 1
                else:
                    marker = "O"
                    q = 2
                pos = pygame.mouse.get_pos()             
                row, column = pos[0] // SpaceBtwRows, pos[1] // SpaceBtwRows
                if cells[row, column] == 0:
                    cells[row, column] = q
                    draw_window(row, column, marker)
                    i += 1
                else:
                    pass                
            print(cells)
        

    pygame.quit()

if __name__ == "__main__":
    grid(WIN, SIZE, ROWS)
    main()