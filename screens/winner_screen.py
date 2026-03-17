import pygame
from utils.constants import WIDTH, HEIGHT
from utils.button import Button

def show_winner(winner):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("🏆 Winner 🏆")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 100)
    text = font.render(f"{winner} Wins!", True, (255, 255, 255))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    back_btn = Button(WIDTH // 2 - 100, HEIGHT // 2, 200, 60, "Back to Menu", (52, 152, 219))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if back_btn.is_clicked(event):
                from screens.menu_screen import menu_screen
                menu_screen()   # quay về menu mà không quit display
                return

        screen.fill((30, 30, 30))
        screen.blit(text, rect)
        back_btn.draw(screen)
        pygame.display.flip()
        clock.tick(60)