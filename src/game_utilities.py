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
