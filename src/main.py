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
    for values in range(BALL_COUNT):
        position = (random.gauss(CANVAS_WIDTH/2, 100), random.gauss(CANVAS_HEIGHT/2, 100))  # noqa: E501
        
        if position[0] < CANVAS_WIDTH // 2:
            velocity = (-1,0)
        elif position[0] > CANVAS_WIDTH // 2:
            velocity = (1,0)
        else:
            velocity = (0,0)

        balls.append(ball.Ball(position,velocity,RADIUS,position[0],CANVAS_WIDTH))
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
        
        dt = clock.tick(60)  # noqa: F841

        game_surface.fill((255, 255, 255))
        info_surface.fill((30,30,30))
        pygame.draw.line(game_surface, (0, 0, 0), (CANVAS_WIDTH // 2, 0), (CANVAS_WIDTH // 2, CANVAS_HEIGHT), 1)  # noqa: E501

        for b in balls:
            b.update(CANVAS_WIDTH,CANVAS_HEIGHT)
            b.ideology_color(CANVAS_WIDTH)
            b.draw(game_surface)

        avgballcolor = BallAnalyzer.average_ball_color(balls)
        text = font.render(f"Avg Color: (R, G, B) = {avgballcolor}", True, (avgballcolor[0], avgballcolor[1], avgballcolor[2]))
        info_surface.blit(text, (10, 10))

        # Draw game in left region
        screen.blit(game_surface, (0, 0))
        # Draw info panel in right region
        screen.blit(info_surface, (CANVAS_WIDTH, 0))

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
