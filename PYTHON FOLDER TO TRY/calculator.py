import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (170, 170, 170)  # Highlight color
FONT = pygame.font.Font(None, 50)

# Button grid (added '⌫' for delete)
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]
delete_button = '⌫'  # Separate delete button

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Calculator")

# Set the app icon
icon = pygame.image.load('Calc.png')  # Load the image into a Surface object
pygame.display.set_icon(icon)  # Set the icon for the window

def draw_buttons(highlighted=None):
    for i, row in enumerate(buttons):
        for j, button in enumerate(row):
            rect = pygame.Rect(j * 100, (i + 1) * 100, 100, 100)

            # Change color if button is highlighted
            color = LIGHT_GRAY if highlighted == (i, j) else GRAY
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

            text = FONT.render(button, True, BLACK)
            screen.blit(text, (rect.x + 35, rect.y + 30))

    # Draw the delete button separately
    delete_rect = pygame.Rect(100, 500, 200, 100)  # Centered at the bottom
    color = LIGHT_GRAY if highlighted == "delete" else GRAY
    pygame.draw.rect(screen, color, delete_rect)
    pygame.draw.rect(screen, BLACK, delete_rect, 2)
    
    text = FONT.render(delete_button, True, BLACK)
    screen.blit(text, (delete_rect.x + 75, delete_rect.y + 30))

def main():
    expression = ""
    running = True
    highlighted_button = None  # Store the currently clicked button

    while running:
        screen.fill(WHITE)
        draw_buttons(highlighted_button)

        # Display input
        text_surface = FONT.render(expression, True, BLACK)
        screen.blit(text_surface, (10, 20))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // 100
                row = (y // 100) - 1

                if 0 <= row < len(buttons) and 0 <= col < len(buttons[row]):
                    highlighted_button = (row, col)  # Highlight the clicked button
                    pygame.display.flip()
                elif 100 <= x <= 300 and 500 <= y <= 600:  # Detecting delete button
                    highlighted_button = "delete"

            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                col = x // 100
                row = (y // 100) - 1

                if 0 <= row < len(buttons) and 0 <= col < len(buttons[row]):
                    button_value = buttons[row][col]
                    if button_value == "C":
                        expression = ""
                    elif button_value == "=":
                        try:
                            expression = str(eval(expression))
                        except Exception:
                            expression = "Error"
                    else:
                        expression += button_value

                elif 100 <= x <= 300 and 500 <= y <= 600:  # Handling delete button click
                    expression = expression[:-1]

                highlighted_button = None  # Remove highlight after clicking

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
