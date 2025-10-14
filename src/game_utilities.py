"""
Class: game_utilities.py
Author: MORS
Date: 5 OCT 25

Description:
Creating a number of game development utilities to potentially help with future projects

Functions:
get_mouse_loc_info - static method that returns the relative mouse position for x number of canvases
TBD ...
"""  
import random

import pygame

import ball
import config
import control_panel as cpanel
from ballanalyzer import BallAnalyzer


class GameUtilities:
    
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
    
    @staticmethod
    def game_init():
        pygame.init()
        icon = pygame.image.load("assets/icons/politaball_icon.png") # Load the original image
        icon = pygame.transform.smoothscale(icon, (32, 32)) # Resize it to 32x32 pixels
        pygame.display.set_icon(icon) # Set the icon for the game
        pygame.display.set_caption("Politaball")

    @staticmethod
    def load_assets():
        font = pygame.font.SysFont(None, 24)
        return(font)

    @staticmethod
    def spawn_balls():
    #Create a list of Balls --
        balls = []

        #generate a randomized list of weights for the social score
        #needs to be moved to another location later
        total = config.BALL_COUNT
        heavy_count = int(total * 0.05)
        medium_count = int(total * 0.10)
        plain_count = total - heavy_count - medium_count

        weights = [3] * heavy_count + [2] * medium_count + [1] * plain_count
        random.shuffle(weights)

                
        for values in range(config.BALL_COUNT):
            position = (random.gauss(config.CANVAS_WIDTH/2, 100), random.gauss(config.CANVAS_HEIGHT/2, 100))  
            if position[0] < config.CANVAS_WIDTH // 2:
                velocity = (-1,0)
            elif position[0] > config.CANVAS_WIDTH // 2:
                velocity = (1,0)
            else:
                velocity = (0,0)

            balls.append(ball.Ball(position,velocity,config.RADIUS,weights[values],config.CANVAS_WIDTH))
        
        return(balls)

    @staticmethod
    def draw_game_panel(screen, balls, game_surface):
        game_surface.fill((255, 255, 255))
        pygame.draw.line(game_surface, (0, 0, 0), (config.CANVAS_WIDTH // 2, 0), (config.CANVAS_WIDTH // 2, config.CANVAS_HEIGHT), 1)
        for b in balls:
            b.draw(game_surface)
        # Draw game in left region
        screen.blit(game_surface, (0, 0))

    @staticmethod
    def update_game_panel(screen, balls, game_surface):
        game_surface.fill((255, 255, 255))
        pygame.draw.line(game_surface, (0, 0, 0), (config.CANVAS_WIDTH // 2, 0), (config.CANVAS_WIDTH // 2, config.CANVAS_HEIGHT), 1)  # noqa: E501

        for b in balls:
            b.neighbor_check(b, balls)
        
        for b in balls:
            b.update(config.CANVAS_WIDTH,config.CANVAS_HEIGHT)
            b.ideology_color(config.CANVAS_WIDTH)
            b.draw(game_surface)
        
        screen.blit(game_surface, (0, 0))

    @staticmethod
    def init_surfaces():
        screen = pygame.display.set_mode((config.CANVAS_WIDTH+config.INFO_PANEL_WIDTH, config.CANVAS_HEIGHT+config.CONTROL_PANEL_HEIGHT))
        game_surface = pygame.Surface((config.CANVAS_WIDTH, config.CANVAS_HEIGHT))
        info_surface = pygame.Surface((config.INFO_PANEL_WIDTH, config.CANVAS_HEIGHT+config.CONTROL_PANEL_HEIGHT))
        control_surface = pygame.Surface((config.CANVAS_WIDTH, config.CONTROL_PANEL_HEIGHT))
        return(screen, game_surface, info_surface, control_surface)

    @staticmethod
    def draw_info_panel(screen, info_surface, font):
        # Info Panel Circle
        info_circle_radius = int(config.INFO_PANEL_WIDTH * 0.45)  # 90% diameter
        info_circle_center = (config.INFO_PANEL_WIDTH // 2, info_circle_radius + 10)
        pygame.draw.circle(info_surface, (255, 0, 0), info_circle_center, info_circle_radius)

        # text = font.render("Avg Color: (R, G, B)", True, (255, 255, 255))
        # info_surface.blit(text, (10, 10))

        # Draw info panel in right region
        screen.blit(info_surface, (config.CANVAS_WIDTH, 0))

    @staticmethod
    def update_info_panel(screen, info_surface, font, balls):
        info_surface.fill((30,30,30))
        avgballcolor = BallAnalyzer.average_ball_color(balls)
        
        # Info Panel Circle
        info_circle_radius = int(config.INFO_PANEL_WIDTH * 0.45)  # 90% diameter
        info_circle_center = (config.INFO_PANEL_WIDTH // 2, info_circle_radius + 10)
        pygame.draw.circle(info_surface, avgballcolor, info_circle_center, info_circle_radius)

        label_text = font.render("Avg Color: ", True, (255,255,255))
        color_text = font.render(f"{avgballcolor}", True, avgballcolor)

        label_rect = label_text.get_rect()
        color_rect = color_text.get_rect()

        total_width = label_rect.width + color_rect.width
        start_x = (config.INFO_PANEL_WIDTH - total_width) // 2
        y_pos = 2 * info_circle_radius + 15

        info_surface.blit(label_text, (start_x, y_pos))
        info_surface.blit(color_text, (start_x + label_rect.width, y_pos))

        screen.blit(info_surface, (config.CANVAS_WIDTH, 0))

    @staticmethod
    def draw_control_panel(screen, control_surface, controlbuttons):
        for button in controlbuttons:
            button.draw_button(control_surface)
        screen.blit(control_surface, (0, config.CANVAS_HEIGHT))

    @staticmethod
    def update_control_panel(screen, control_surface, controlbuttons):
        control_surface.fill((0,0,0))
        for button in controlbuttons: #updates the control panel - may need to refactor this later
                button.draw_button(control_surface)
        screen.blit(control_surface, (0, config.CANVAS_HEIGHT))
    
