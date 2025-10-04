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
import pygame.gfxdraw


class Ball:

    ballcount = 0
    red_avg = 0
    blue_avg = 0

    def __init__(self, position, velocity, radius, social,canvas_width):
        self.position = pygame.math.Vector2(position)      # PyGame Vector2 object
        self.velocity = pygame.math.Vector2(velocity)      # PyGame Vector2 object
        self.radius = radius
        self.social = social          # social score
        self.ideology_color(canvas_width)
        Ball.ballcount += 1

    def update(self, screen_width, screen_height):
        # Move the ball
        if self.velocity[0] != 0:
            self.position[0] += self.velocity[0]
            if self.position[0] <= self.radius:
                self.position[0] = self.radius
                self.velocity[0] = 0
            elif self.position[0] >= (screen_width - self.radius):
                self.position[0] = (screen_width - self.radius)
                self.velocity[0] = 0

        if self.velocity[1] !=0:
            self.position[1] += self.velocity[1]
            if self.position[1] <= self.radius:
                self.position[1] = self.radius
                self.velocity[1] = 0
            elif self.position[1] >= (screen_height - self.radius):
                self.position[1] = (screen_height - self.radius)
                self.velocity[1] = 0

    def draw(self, surface):
        # Draw the ball on the specified surface -in this case we pass the variable screen
        #pygame.draw.circle(surface, self.color,  self.position, self.radius) #basic circle # noqa: E501
        #pygame.draw.circle(surface, (0,0,0),  self.position, self.radius, 1) #basic circle outline # noqa: E501
        pygame.gfxdraw.filled_circle(surface, int(self.position.x), int(self.position.y), self.radius, self.color)  # noqa: E501
        pygame.gfxdraw.aacircle(surface, int(self.position.x), int(self.position.y), self.radius, (0,0,0))  # noqa: E501


    def speed(self):
        # Return scalar speed
        return (self.velocity[0]**2 + self.velocity[1]**2)**0.5

    def direction(self):
        # Return angle in degrees or radians
        return math.atan2(self.velocity[1], self.velocity[0])
    
    def ideology_color(self, canvas_width):
        # Alter a ball's color based on where it is from left(blue) to right (red)
        #ratio = self.position.x / canvas_width
        ratio = max(0, min(1,self.position.x / canvas_width))
        r = int(255 * ratio)
        b = int(255 * (1 - ratio))
        self.color =  (r, 0, b)
    
    @classmethod
    def get_ball_count(cls):
        return f"Total # of balls: {cls.ballcount}"
    
    @classmethod
    def get_avg_color(cls):
        red = cls.red_avg / cls.ballcount
        blue = cls.blue_avg / cls.ballcount
        return f"The average color is: ({red}, 0, {blue})"


