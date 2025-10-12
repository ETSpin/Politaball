"""
Class: {file_name}
Author: MORS
Date: {date}

Description:
{brief_description_of_the_file}

Usage:
{brief_usage_instructions}

"""

import pygame


class GUIElements:
    gui_item_count = 0

    def __init__(self, visible = False, gui_item_type = "GUI_Item", name = "Unnamed_GUI_Item"):
        
        self.visible = visible
        self.gui_item_type = gui_item_type
        self.name = name
        self.gui_item_number = GUIElements.gui_item_count

        GUIElements.gui_item_count +=1

class Button(GUIElements):
    buttoncount = 0

    def __init__(self, text, x, y, width, height, font, buttonname = None, visible=True, textcolor=(255,255,255), buttoncolor=(211,211,211)):
        super().__init__(visible, "Button_Item", f"button{Button.buttoncount}")
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.textcolor = textcolor
        self.buttoncolor = buttoncolor
        self.text = text
        self.button_number = Button.buttoncount
        if buttonname is None:
            self.name = f"button_{Button.buttoncount}"
        else:
            self.name = buttonname
        self._rect = pygame.Rect(self.x, self.y, self.width, self.height)

        Button.buttoncount +=1
    
    def draw_button(self, surface):  # noqa: E501
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.buttoncolor, self._rect, 0 , 5)
        button_text = self.font.render(self.text, True, self.textcolor)
        button_rect = button_text.get_rect()
        button_rect.center = rect.center
        surface.blit(button_text, button_rect)

    def is_clicked(self, pos):
        return self._rect.collidepoint(pos)

    @property
    def left(self):
        return self._rect.left

    @property
    def right(self):
        return self._rect.right
    
    @property
    def center(self):
        return self._rect.center
    
    @property
    def top(self):
        return self._rect.top

    @property
    def bottom(self):
        return self._rect.bottom

    @property
    def topleft(self):
        return self._rect.topleft
    
    @property
    def topright(self):
        return self._rect.topright
    
    @property
    def bottomleft(self):
        return self._rect.bottomleft
    
    @property
    def bottomright(self):
        return self._rect.bottomright