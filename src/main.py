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

    #CONSTANTS
    CANVAS_WIDTH = 1200
    CANVAS_HEIGHT = 1200
    BALL_COUNT = 1000
    # GREY = (128, 128, 128)
    # MAGENTA = (255, 0, 255)
    # BLUE = (0, 0 , 255)
    # RED = (255, 0, 0)
    RADIUS = 5


    #Create a list of Balls --
    balls = []

    for values in range(BALL_COUNT):
        position = (random.gauss(CANVAS_WIDTH/2, 100), random.gauss(CANVAS_HEIGHT/2, 100))  # noqa: E501
        velocity = (0,0)
        color = ball.Ball.ideology_color(position[0], CANVAS_WIDTH)
        balls.append(ball.Ball(position,velocity,RADIUS,position[0],color))
    print(ball.Ball.get_ball_count())
    
    pygame.init()
    icon = pygame.image.load("assets/icons/politaball_icon.png") # Load the original image
    icon = pygame.transform.smoothscale(icon, (32, 32)) # Resize it to 32x32 pixels
    pygame.display.set_icon(icon) # Set the icon for the game
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("Politaball")
    
    #Start the Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
      
        pygame.draw.line(screen, (0, 0, 0), (CANVAS_WIDTH // 2, 0), (CANVAS_WIDTH // 2, CANVAS_HEIGHT), 1)  # noqa: E501

        for b in balls:
            b.draw(screen)

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
