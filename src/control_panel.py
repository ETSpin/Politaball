#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
File: control_panel.py
Author: MORS
Date: 12 Oct 25

Description:
Build the Control Panel for the game by creating a series of helper functions

Usage:
create buttons -- create the buttons in the control surface of the game

"""
import game_utilities as game_utils
import gui_elements


@staticmethod
def create_buttons(control_surface, font):
    control_rect = control_surface.get_rect()
    button_width, button_height = 100, 50
    padding = 5
    center_button_x = control_rect.centerx - button_width // 2
    center_button_y = control_rect.centery - button_height // 2

    step_button = gui_elements.Button("Step",center_button_x ,center_button_y,button_width,button_height,font,"step_button")  # noqa: E501
    pause_button = gui_elements.Button("Pause",step_button.left - (button_width + padding),center_button_y,button_width,button_height,font,"pause_button")  # noqa: E501
    play_button = gui_elements.Button("Play",step_button.right + padding,center_button_y,button_width,button_height,font,"play_button")  # noqa: E501

    return (step_button, pause_button, play_button)

@staticmethod
def check_button_click(buttons, mouse_info):
    for button in buttons:
        _, pos = mouse_info
        if button.is_clicked(pos):
            print(button.name)
            return(button.name)

