import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color=None, text_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.base_color = color
        self.hover_color = hover_color if hover_color else (
            min(color[0]+40,255), min(color[1]+40,255), min(color[2]+40,255))
        self.text_color = text_color
        self.font = pygame.font.Font(None, 40)

        try:
            self.click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
        except:
            self.click_sound = None

    def draw(self, screen):
        # 🔹 Kiểm tra pygame còn hoạt động không
        if not pygame.get_init():
            return

        try:
            mouse_pos = pygame.mouse.get_pos()
        except pygame.error:
            return

        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.base_color

        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2, border_radius=12)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        # 🔹 Nếu pygame chưa khởi tạo hoặc đã quit → bỏ qua
        if not pygame.get_init():
            return False

        try:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    if self.click_sound:
                        self.click_sound.play()
                    return True
        except pygame.error:
            return False

        return False
