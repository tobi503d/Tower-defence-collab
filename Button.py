from dataclasses import dataclass
import pygame

@dataclass
class buttonStyle:
    colorBG: tuple
    colorText: tuple
    colorHover: tuple
    colorPressed: tuple = None

@dataclass
class button:
    rect: pygame.Rect
    text: str
    style: buttonStyle
    onClick: callable = None
    onePress: bool = False
    _hovered: bool = False
    _pressed: bool = False

    def update(self, screen):
        mousePos = pygame.mouse.get_pos()
        mousePressed = pygame.mouse.get_pressed()[0]

        self._hovered = self.rect.collidepoint(mousePos)

        if self._hovered and mousePressed and not self._pressed:
            self._pressed = True
            if self.onClick:
                self.onClick()
        elif not mousePressed:
            self._pressed = False

        if self._hovered:
            color = self.style.colorHover
        else:
            color = self.style.colorBG
        pygame.draw.rect(screen, color, self.rect, border_radius=6)