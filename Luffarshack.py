import pygame

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 60 

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_window():
    WIN.fill(WHITE)
pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()