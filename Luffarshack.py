import pygame
import numpy as np
import os
import time

SIZE = 600
ROWS = 20
WIN = pygame.display.set_mode((SIZE, SIZE))
SpaceBtwRows = SIZE // ROWS
FPS = 60 

points_x = 0
points_o = 0

# Importera kryss, cirkel och ändra storleken
CROSS_IMAGE = pygame.image.load(os.path.join('cross.png'))
CROSS_IMAGE = pygame.transform.scale(CROSS_IMAGE, (24, 24))
CIRKEL_IMAGE = pygame.image.load(os.path.join('cirkel.png'))
CIRKEL_IMAGE = pygame.transform.scale(CIRKEL_IMAGE, (32, 32))

# Använder np.zeros för att göra en 20 * 20 array fyld med nollor
cells = np.zeros((ROWS,ROWS), dtype=int)

# Färger för trevlighetens skull
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Funktion för att rita upp ett 20 * 20 grid
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

# Funktion för att rita kryss eller cirkel
def draw_window(row, column, marker):
    x = row * SpaceBtwRows
    y = column * SpaceBtwRows
    if marker == "O":
        WIN.blit(CIRKEL_IMAGE, (x - 1, y - 1))
    else:
        WIN.blit(CROSS_IMAGE, (x + 3, y + 3))
    pygame.display.update()

# Funktion för att rita ett streck när någon får 5 i rad
def draw_win(win):
    row_from, column_from = win[0]
    row_to, column_to = win[1]
    pygame.draw.line(WIN, (BLUE),
                     (row_from * SpaceBtwRows + 15, column_from * SpaceBtwRows + 15),
                     (row_to * SpaceBtwRows + 15, column_to * SpaceBtwRows + 15), 5)
    pygame.display.update()

# Funktion för att kolla om någon vunnit 
def check_win(placedX: int, placedY: int, length: int=5):
     
    startCell = cells[placedX][placedY]
    # Axlarna som man kan vinna i
    axlar = [
        (1, 0), # Horisontellt
        (0, 1), # Vertikalt 
        (1, 1), # Diagonalt upp vänster till ner höger 
        (1, -1) # Diagonalt ner vänster till upp höger
    ]
    # Kollar vinnst för alla axlar 
    for stepX, stepY in axlar:
        # Kollar vinst för alla avstånd 
        for offset in range(-length+1, 1):
            for i in range(0, length):
                try:
                    x = placedX+stepX*(offset+i)
                    y = placedY+stepY*(offset+i)
                    if cells[x][y] != startCell:
                        break
                except IndexError:
                    break
            # Om allt går som det ska
            else:
                # Retunera start och slut kordinaterna för vinsten 
                return [(placedX+stepX*offset, placedY+stepY*offset),
                        (placedX+stepX*(offset+length-1), placedY+stepY*(offset+length-1))]
    return None
                
# Main funktionen som styr allt 
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
            # Kollar vems tur det är att spela
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if i % 2 == 0:
                    marker = "X"
                    q = 1
                else:
                    marker = "O"
                    q = 2
                pos = pygame.mouse.get_pos() 
                # Delar värdet på pixeln man klickade på med avståndet mellan linjerna för att räkna ut vilken ruta man tryckte på              
                row, column = pos[0] // SpaceBtwRows, pos[1] // SpaceBtwRows
                # Kollar om der redan är något placerat i den rutan man trycker på, om det inte är det så placeras ett kryss eller cirkel beroende på vems tur det är
                if cells[row, column] == 0:
                    # Byter ut nollan i den 20 * 20 arrayen för den plats som blev klickad på med en etta eller tvåa beroende på vems tur det är 
                    cells[row, column] = q
                    draw_window(row, column, marker)
                    i += 1
                else:
                    pass                
                # När någon har lagt så kallar vi på funktionen som kollar om någon vunnit 
                Win = check_win(row, column, 5)
                if Win: 
                    draw_win(Win)
                    # Ändrar poängställningen i spelrutans namn 
                    global points_o
                    global points_x
                    if i % 2 == 0:
                        points_o += 1
                    else:
                        points_x += 1
                    xstr = str(points_x)
                    ostr = str(points_o)
                    pygame.display.set_caption("Kryss " + xstr + " poäng" + " VS " + "Cirkels " + ostr + " poäng ")
                    # När någon vinner så fryser rutan och börgar om
                    time.sleep(3.0)
                    pygame.event.clear()
                    cells.fill(0)
                    grid(WIN, SIZE, ROWS)

    pygame.quit()

if __name__ == "__main__":
    grid(WIN, SIZE, ROWS)
    main()