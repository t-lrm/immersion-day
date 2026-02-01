import time
import pygame


class Display:

    def __init__(self):
        self._memory = [False] * (32 * 64)
        self.pixel_size = 10

        pygame.init()
        self.screen = pygame.display.set_mode((64 * self.pixel_size, 32 * self.pixel_size))
        pygame.display.set_caption("CHIP-8 Emulator")
        self.clear()

    def __getitem__(self, i):
        return self._memory[i]

    def __setitem__(self, i, value):
        if self._memory[i] == value:
            return

        self._memory[i] = value

        color = (255, 255, 255) if value else (0, 0, 0)
        x = i % 64
        y = i // 64
        pygame.draw.rect(self.screen, color,(x * self.pixel_size, y * self.pixel_size, self.pixel_size, self.pixel_size))

    def clear(self):
        """Clears the screen by filling it with black."""
        for i in range(len(self._memory)):
            self._memory[i] = False
        self.screen.fill((0, 0, 0))  # Fill screen with black

    def draw(self):
        """Draws the current pixel grid to the screen."""
        pygame.display.flip()  # Update the display

    def update(self):
        """Handles events and updates the display."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

