import pygame
pygame.init()
pygame.display.set_caption("for loops")
screen = pygame.display.set_mode((800, 800))

while True:
    
    event = pygame.event.wait()
    
    if event.type == pygame.QUIT:
        break
    
    
    for i in range (10):
        pygame.draw.rect(screen, (100, 0, 100), (i*80, 50, 20, 20))
    pygame.display.flip()
    
    
pygame.quit() 
