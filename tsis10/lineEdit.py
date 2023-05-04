import pygame

import var


class LineEdit(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, screen):
        super().__init__()
        self.non_active_color = (255, 255, 255)
        self.active_color = pygame.Color("#FFD700")
        self.color = self.non_active_color
        self.backcolor = None
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.width = w
        self.height = h
        self.font_size = 50
        self.font = pygame.font.SysFont("comicsansms", self.font_size)
        self.active = False
        self.text = ""
        self.screen = screen
        self.render_text()

    # Отрисовка LineEdit на экране
    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((self.width, self.height),
                                    pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (12, (self.height - t_surf.get_height()) // 2))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.screen.blit(self.image, (self.x, self.y))

    # Реализация изменения текста в LineEdit
    def update(self):
        var.user = self.text
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    var.start = False
                    var.game_over = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)
            if self.active:
                self.color = self.active_color
            else:
                self.color = self.non_active_color
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < 15 and event.key != pygame.K_BACKSPACE:
                    self.text += event.unicode.upper()
        self.render_text()
        return self.text