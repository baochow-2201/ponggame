import pygame, math
from utils.constants import WIDTH, HEIGHT
from utils.button import Button

def menu_screen():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("🏓 Pong Game Menu 🏓")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 80)
    title = font.render(" Pong Game ", True, (255, 255, 255))
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4))

    play_ai = Button(WIDTH//2 - 120, HEIGHT//2 - 60, 240, 60, "Play vs AI", (52, 152, 219))
    play_2p = Button(WIDTH//2 - 120, HEIGHT//2 + 20, 240, 60, "2 Player Mode", (46, 204, 113))
    quit_btn = Button(WIDTH//2 - 120, HEIGHT//2 + 100, 240, 60, "Quit", (231, 76, 60))

    running = True
    color_shift = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if play_ai.is_clicked(event):
                from game.pong import pong_game
                pong_game(vs_ai=True)
            if play_2p.is_clicked(event):
                from game.pong import pong_game
                pong_game(vs_ai=False)
            if quit_btn.is_clicked(event):
                running = False

        # Nền gradient động
        color_shift += 0.05
        r = int(min(max(50 + 40 * (1 + math.sin(color_shift * 0.4)), 0), 255))
        g = int(min(max(70 + 60 * (1 + math.sin(color_shift * 0.5)), 0), 255))
        b = int(min(max(150 + 80 * (1 + math.sin(color_shift * 0.3)), 0), 255))
        screen.fill((r, g, b))

        # Vẽ tiêu đề và nút
        screen.blit(title, title_rect)
        play_ai.draw(screen)
        play_2p.draw(screen)
        quit_btn.draw(screen)

        pygame.display.flip()
        clock.tick(60)
