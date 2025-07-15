import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sports Car Text Fade-In")

# Colors (inspired by a sleek sports car)
RED = (200, 0, 0)  # Vibrant car red
BLACK = (0, 0, 0)  # Background
WHITE = (255, 255, 255)  # For text outline or accents

# Font setup
font = pygame.font.SysFont("impact", 72)  # Bold, sporty font
text_content = "VROOM!"
text = font.render(text_content, True, RED)
text_rect = text.get_rect(center=(width // 2, height // 2))

# Animation settings
fade_duration = 2.0  # Seconds for fade-in
start_time = time.time()
alpha = 0  # Start fully transparent

# Background (simple gradient for speed effect)
def draw_background():
    for y in range(height):
        color = (0, 0, min(50 + y // 3, 255))  # Dark to bluish gradient
        pygame.draw.line(screen, color, (0, y), (width, y))

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate alpha based on time
    elapsed = time.time() - start_time
    if elapsed < fade_duration:
        alpha = int(255 * (elapsed / fade_duration))  # Linear fade
    else:
        alpha = 255  # Fully opaque

    # Draw background
    draw_background()

    # Create a surface for the text with alpha
    text_surface = font.render(text_content, True, RED)
    text_surface.set_alpha(alpha)

    # Draw text
    screen.blit(text_surface, text_rect)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

    # Exit after fade-in completes (optional)
    if elapsed > fade_duration + 2:  # Hold for 2 seconds after fade
        running = False

# Clean up
pygame.quit()
sys.exit()