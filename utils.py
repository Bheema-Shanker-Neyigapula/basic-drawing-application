import os
import pygame

def save_drawing(surface):
    filename = "drawing.png"
    pygame.image.save(surface, filename)
    print("Drawing saved as:", filename)

def load_drawing(screen):
    filename = "drawing.png"
    if pygame.image.get_extended():
        if os.path.exists(filename):
            loaded_image = pygame.image.load(filename)
            screen.blit(loaded_image, (0, 0))
            pygame.display.flip()
            print("Drawing loaded successfully")
        else:
            print("No saved drawing found")
