#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
File: main.py
Author: MORS
Date: 21 Sep 25

Description:
Politaball -- minor variations can move things

Usage:

"""
def main():

    import copy
    import math  # noqa: F401
    import random

    import pygame

    import ball
    import config
    import control_panel as cpanel
    import gui_elements  # noqa: F401
    from game_utilities import GameUtilities as game_utils

    #initialize pygame and setup the screen layout
    game_utils.game_init()
    clock = pygame.time.Clock()     # Set the clock start time -- used for FPS calculations in game loop
    font = game_utils.load_assets()
    screen, game_surface, info_surface, control_surface = game_utils.init_surfaces()
    balls = game_utils.spawn_balls()
    controlbuttons = cpanel.create_buttons(control_surface, font)

    #Draw the panels
    game_utils.draw_info_panel(screen, info_surface, font)
    game_utils.draw_game_panel(screen, balls, game_surface)
    game_utils.draw_control_panel(screen, control_surface, controlbuttons)

    #Start the Game Loop
    running = True
    paused = False
    step_once = False
    while running:
        # Sets FPS to 60
        dt = clock.tick(config.FPS)  # noqa: F841
        if not paused:           
            game_utils.update_game_panel(screen, balls, game_surface)
            game_utils.update_info_panel(screen, info_surface, font, balls)
            game_utils.update_control_panel(screen, control_surface, controlbuttons)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 print(f"Mouse clicked at: {pygame.mouse.get_pos()}")
                 mouse_pos = event.pos
                 click_location_check = game_utils.get_mouse_loc_info(mouse_pos, game=(game_surface,(0,0)), control=(control_surface,(0, config.CANVAS_HEIGHT)), info=(info_surface,(config.CANVAS_WIDTH,0)))  # noqa: E501
                 buttonclicked = cpanel.check_button_click(controlbuttons, click_location_check)
                 
                 if buttonclicked == "step_button":
                    print("Step button clicked")
                 elif buttonclicked == "pause_button":
                    print("Pause button clicked")
                    paused = True
                 elif buttonclicked == "play_button":
                    print("Play button clicked")
                    paused = False
                 else:
                    pass


        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
