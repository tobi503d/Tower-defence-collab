from dataclasses import dataclass
import pygame

@dataclass  # inwstead of def __init__ and self.x
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
    fontSize: int
    onClick: callable = None
    onePress: bool = False
    _hovered: bool = False
    _pressed: bool = False

    def __post_init__(self):
        self.font = pygame.font.Font(None, self.fontSize)
        self.textDisplay = self.font.render(self.text, True, self.style.colorText)
        self.textRect = self.textDisplay.get_rect(center=self.rect.center)
        

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
        screen.blit(self.textDisplay, self.textRect)
        