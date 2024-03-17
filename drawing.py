import pygame
from ml_model import MLModel

class DrawingApp:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 600
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Shape Classifier")
        self.ml_model = MLModel()
        self.drawing = False
        self.last_pos = None
        self.radius = 20
        self.current_shape = []
        self.current_color = self.BLACK

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drawing = True
                    self.current_shape.append(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.drawing = False
                    shape_label = self.ml_model.classify_shape(self.screen.copy())
                    print("Predicted Shape:", shape_label)
                    self.current_shape = []
            elif event.type == pygame.MOUSEMOTION:
                if self.drawing:
                    self.current_shape.append(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:  # Clear canvas
                    self.screen.fill(self.WHITE)
                    self.current_shape = []
                elif event.key == pygame.K_s:  # Save drawing
                    self.save_drawing()
                elif event.key == pygame.K_l:  # Load drawing
                    self.load_drawing()
                # Handle color selection, shape selection, etc.

    def save_drawing(self):
        filename = "drawing.png"
        pygame.image.save(self.screen, filename)
        print("Drawing saved as:", filename)

    def load_drawing(self):
        filename = "drawing.png"
        if pygame.image.get_extended():
            if os.path.exists(filename):
                loaded_image = pygame.image.load(filename)
                self.screen.blit(loaded_image, (0, 0))
                pygame.display.flip()
                print("Drawing loaded successfully")
            else:
                print("No saved drawing found")

    def draw_shape(self):
        if len(self.current_shape) < 2:
            return
        # Draw shapes based on current_shape list

    def run(self):
        while True:
            self.handle_events()
            self.screen.fill(self.WHITE)
            self.draw_shape()
            pygame.display.flip()
