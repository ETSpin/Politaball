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
    import random  # noqa: F401

    import pygame

    import ball  # noqa: F401
    from ballanalyzer import BallAnalyzer

    #CONSTANTS
    CANVAS_WIDTH = 1200
    INFO_PANEL_WIDTH = 300
    CANVAS_HEIGHT = 1200
    BALL_COUNT = 1000
    # GREY = (128, 128, 128)
    # MAGENTA = (255, 0, 255)
    # BLUE = (0, 0 , 255)
    # RED = (255, 0, 0)
    RADIUS = 5

    #ballanalysis = BallAnalyzer()

    #Create a list of Balls --
    balls = []
    starting_balls = []
    for values in range(BALL_COUNT):
        position = (random.gauss(CANVAS_WIDTH/2, 100), random.gauss(CANVAS_HEIGHT/2, 100))  # noqa: E501
        
        if position[0] < CANVAS_WIDTH // 2:
            velocity = (-1,0)
        elif position[0] > CANVAS_WIDTH // 2:
            velocity = (1,0)
        else:
            velocity = (0,0)

        balls.append(ball.Ball(position,velocity,RADIUS,position[0],CANVAS_WIDTH))
    
    starting_balls = copy.deepcopy(balls) #captures the starting state of the balls
    print(ball.Ball.get_ball_count())
    
    #initialize pygame
    pygame.init()
    icon = pygame.image.load("assets/icons/politaball_icon.png") # Load the original image
    icon = pygame.transform.smoothscale(icon, (32, 32)) # Resize it to 32x32 pixels
    pygame.display.set_icon(icon) # Set the icon for the game
    screen = pygame.display.set_mode((CANVAS_WIDTH+INFO_PANEL_WIDTH, CANVAS_HEIGHT))
    font = pygame.font.SysFont(None, 24)
    game_surface = pygame.Surface((CANVAS_WIDTH, CANVAS_HEIGHT))
    info_surface = pygame.Surface((INFO_PANEL_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("Politaball")

    # Info Panel Circle
    info_circle_radius = int(INFO_PANEL_WIDTH * 0.45)  # 90% diameter
    info_circle_center = (INFO_PANEL_WIDTH // 2, info_circle_radius + 10)
    pygame.draw.circle(info_surface, (255, 0, 0), info_circle_center, info_circle_radius)

    # Set the clock start time -- used for FPS calculations in game loop
    clock = pygame.time.Clock()


    #load the initial state of the balls onto the screen
    for b in balls:
        b.draw(game_surface)

    text = font.render("Avg Color: (R, G, B)", True, (255, 255, 255))
    info_surface.blit(text, (10, 10))
    # Draw game in left region
    screen.blit(game_surface, (0, 0))
    # Draw info panel in right region
    screen.blit(info_surface, (CANVAS_WIDTH, 0))

    
    #Start the Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Sets FPS to 60
        dt = clock.tick(60)  # noqa: F841

        game_surface.fill((255, 255, 255))
        info_surface.fill((30,30,30))
        pygame.draw.line(game_surface, (0, 0, 0), (CANVAS_WIDTH // 2, 0), (CANVAS_WIDTH // 2, CANVAS_HEIGHT), 1)  # noqa: E501

        for b in balls:
            b.update(CANVAS_WIDTH,CANVAS_HEIGHT)
            b.ideology_color(CANVAS_WIDTH)
            b.draw(game_surface)

        avgballcolor = BallAnalyzer.average_ball_color(balls)
        pygame.draw.circle(info_surface, avgballcolor, info_circle_center, info_circle_radius)  # noqa: E501

        label_text = font.render("Avg Color: ", True, (255,255,255))
        color_text = font.render(f"{avgballcolor}", True, avgballcolor)

        label_rect = label_text.get_rect()
        color_rect = color_text.get_rect()

        total_width = label_rect.width + color_rect.width
        start_x = (INFO_PANEL_WIDTH - total_width) // 2
        y_pos = 2 * info_circle_radius + 15

        info_surface.blit(label_text, (start_x, y_pos))
        info_surface.blit(color_text, (start_x + label_rect.width, y_pos))



        # Draw game in left region
        screen.blit(game_surface, (0, 0))
        # Draw info panel in right region
        screen.blit(info_surface, (CANVAS_WIDTH, 0))

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
