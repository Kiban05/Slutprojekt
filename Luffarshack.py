import pygame

SIZE = 600
ROWS = 20
WIN = pygame.display.set_mode((SIZE, SIZE))
SpaceBtwRows = SIZE // ROWS
FPS = 60 

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
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()