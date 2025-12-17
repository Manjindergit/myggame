import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    player1 = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    
    while True:
        log_state()
        player1.draw(screen)
        clock = pygame.time.Clock()
        dt = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        player1.draw(screen)
        pygame.display.flip()
        
        clock.tick(60)
        dt = clock.get_time() / 1000
        

if __name__ == "__main__":
    main()
