"""
Class: ball
Author: MORS
Date: 21 Sep 25

Description:
This class is designed to create "ball" objects 

Usage:
You should be able to create object of the type ball with this class library

"""
import math  # noqa: F401
import random  # noqa: F401

import pygame


class Ball:
    def __init__(self, position, velocity, radius, social, color):
        self.position = pygame.math.Vector2(position)      # PyGame Vector2 object
        self.velocity = pygame.math.Vector2(velocity)      # PyGame Vector2 object
        self.radius = radius
        self.social = social          # social score
        self.color = color

    def update(self):
        # Move the ball
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        # Add boundary logic here if needed

    def draw(self, surface):
        # Draw the ball on the given surface
        pygame.draw.circle(surface, self.color, self.position, self.radius)

    def speed(self):
        # Return scalar speed
        return (self.velocity[0]**2 + self.velocity[1]**2)**0.5

    def direction(self):
        # Return angle in degrees or radians
        return math.atan2(self.velocity[1], self.velocity[0])
    
    def ideology_color(x, canvas_width):
        # Alter a ball's color based on where it is from left(blue) to right (red)
        ratio = x / canvas_width
        r = int(255 * ratio)
        b = int(255 * (1 - ratio))
        return (r, 0, b)

