"""
Class: game_utilities.py
Author: MORS
Date: 5 OCT 25

Description:
Creating a number of game development utilities to help with future projects

Functions:
draw_menu_button - static method to draw and return a simple grey button with black text
get_mouse_loc_info - static method that returns the relative mouse position for x number of canvases
TBD ...
"""  # noqa: E501
import pygame


class Game_Utilities:
    
    # draws and returns a simple grey button with black text
    @staticmethod
    def draw_menu_button(surface, text, x, y, width, height, font, textcolor=(255,255,255), buttoncolor=(211,211,211)):  # noqa: E501
        button = pygame.Rect(x,y,width,height) 
        pygame.draw.rect(surface, buttoncolor, button, 0,5)
        button_text = font.render(text, True, textcolor)
        button_rect = button_text.get_rect()
        button_rect.center = button.center
        surface.blit(button_text, button_rect)
        return button
    
    # a method to find the relative mouse position for several pygame surfaces
    @staticmethod
    def get_mouse_loc_info(mouse_pos, **surface_origins):
        for name, (surface, origin) in surface_origins.items():
            surface_rect = pygame.Rect(origin, surface.get_size())
            if surface_rect.collidepoint(mouse_pos):
                relativemousepos = (mouse_pos[0] - origin[0], mouse_pos[1] - origin[1])
                #print(f"surface locations: {surface_rect}")
                #print(f"relative mouse position: {relativemousepos}")   
                return(surface, relativemousepos)
        return (None, None)
