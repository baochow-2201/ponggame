import pygame, sys, random
from utils.constants import WIDTH, HEIGHT
from screens.winner_screen import show_winner
from screens.pause_screen import pause_screen

def pong_game(vs_ai=True):
    pygame.display.quit()
    pygame.display.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("🏓 Pong Game")
    clock = pygame.time.Clock()

    # ====== KHỞI TẠO CÁC BIẾN ======
    ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
    player = pygame.Rect(WIDTH - 30, HEIGHT//2 - 70, 10, 140)
    opponent = pygame.Rect(20, HEIGHT//2 - 70, 10, 140)

    ball_speed_x, ball_speed_y = 6, 6
    player_speed, opponent_speed = 0, 6
    player_score, opponent_score = 0, 0
    font = pygame.font.Font(None, 74)
    ball_color = (255, 255, 255)  # màu ban đầu

    # ====== HÀM PHỤ ======
    def restart_game():
        nonlocal ball, player, opponent, player_score, opponent_score, ball_speed_x, ball_speed_y, ball_color
        ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
        player = pygame.Rect(WIDTH - 30, HEIGHT//2 - 70, 10, 140)
        opponent = pygame.Rect(20, HEIGHT//2 - 70, 10, 140)
        player_score = opponent_score = 0
        ball_speed_x, ball_speed_y = 6, 6
        ball_color = (255, 255, 255)

    def random_color():
        """Tạo màu ngẫu nhiên sáng"""
        return (
            random.randint(80, 255),
            random.randint(80, 255),
            random.randint(80, 255)
        )

    # ====== VÒNG LẶP CHÍNH ======
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed = 6
                if event.key == pygame.K_UP:
                    player_speed = -6
                if event.key == pygame.K_ESCAPE:
                    action = pause_screen(screen, clock, resume_callback=None, restart_callback=restart_game)
                    if action in ["quit", "menu"]:
                        return
                    if action == "restart":
                        restart_game()
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_DOWN, pygame.K_UP]:
                    player_speed = 0

        # ====== CẬP NHẬT VỊ TRÍ ======
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        player.y += player_speed

        # ====== ĐIỀU KHIỂN AI HOẶC NGƯỜI CHƠI 2 ======
        if vs_ai:
            if opponent.centery < ball.centery:
                opponent.y += opponent_speed
            elif opponent.centery > ball.centery:
                opponent.y -= opponent_speed
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                opponent.y -= opponent_speed
            if keys[pygame.K_s]:
                opponent.y += opponent_speed

        # ====== XỬ LÝ VA CHẠM ======
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        if ball.left <= 0:
            player_score += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x *= -1
            ball_color = (255, 255, 255)

        if ball.right >= WIDTH:
            opponent_score += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x *= -1
            ball_color = (255, 255, 255)

        # Bóng chạm paddle → bật lại + đổi màu 🎨
        if ball.colliderect(player) or ball.colliderect(opponent):
            ball_speed_x *= -1
            ball_color = random_color()

        # Giới hạn paddle trong màn hình
        player.clamp_ip(screen.get_rect())
        opponent.clamp_ip(screen.get_rect())

        # ====== VẼ MÀN HÌNH ======
        screen.fill((35, 0, 70))
        pygame.draw.rect(screen, (255, 255, 255), player)
        pygame.draw.rect(screen, (255, 255, 255), opponent)
        pygame.draw.ellipse(screen, ball_color, ball)  # Bóng đổi màu ở đây
        pygame.draw.aaline(screen, (255, 255, 255), (WIDTH//2, 0), (WIDTH//2, HEIGHT))

        text = font.render(f"{opponent_score} - {player_score}", True, (255, 255, 255))
        screen.blit(text, (WIDTH//2 - 50, 20))

        pygame.display.flip()
        clock.tick(60)

        # ====== KIỂM TRA KẾT THÚC TRẬN ======
        if player_score == 5 or opponent_score == 5:
            winner = "Player 1" if player_score == 5 else "Opponent"
            show_winner(winner)
            return
