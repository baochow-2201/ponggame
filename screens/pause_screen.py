import pygame
from utils.button import Button
from utils.constants import WIDTH, HEIGHT

def pause_screen(screen, clock, resume_callback, restart_callback):
    """Hiển thị menu Pause trên màn hình hiện tại"""
    font = pygame.font.Font(None, 100)
    text = font.render("PAUSED", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))

    resume_btn = Button(WIDTH//2 - 100, HEIGHT//2 - 40, 200, 60, "Resume", (46, 204, 113))
    restart_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 40, 200, 60, "Restart", (52, 152, 219))
    menu_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 120, 200, 60, "Main Menu", (241, 196, 15))
    quit_btn = Button(WIDTH//2 - 100, HEIGHT//2 + 200, 200, 60, "Quit", (231, 76, 60))

    running = True
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(150)
    overlay.fill((20, 30, 60))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if resume_btn.is_clicked(event):
                return "resume"
            if restart_btn.is_clicked(event):
                restart_callback()
                return "restart"
            if menu_btn.is_clicked(event):
                from screens.menu_screen import menu_screen
                menu_screen()
                return "menu"
            if quit_btn.is_clicked(event):
                pygame.quit()
                return "quit"

        screen.blit(overlay, (0, 0))
        screen.blit(text, text_rect)
        resume_btn.draw(screen)
        restart_btn.draw(screen)
        menu_btn.draw(screen)
        quit_btn.draw(screen)

        pygame.display.flip()
        clock.tick(60)
