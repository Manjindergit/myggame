import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    
    print("Starting Asteroids with pygame version: VERSION")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    
    player1 = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = pygame.time.Clock().tick(60) / 1000.0  # Delta time in seconds
        updateable.update(dt)
        screen.fill((0, 0, 0))  # Clear screen with black
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        
           
        
        

if __name__ == "__main__":
    main()
