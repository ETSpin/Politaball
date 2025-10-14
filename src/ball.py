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

import config


class Ball:

    ballcount = 0
    red_avg = 0
    blue_avg = 0

    def __init__(self, position, velocity, radius, social, canvas_width):
        self.position = pygame.math.Vector2(position)      # PyGame Vector2 object
        self.velocity = pygame.math.Vector2((1,0))      # PyGame Vector2 object
        self.radius = radius
        self.social = social          # social score
        self.ideology_color(canvas_width)
        self.position_snapshot = self.position.copy()
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
        #draw a ball
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
        ratio = max(0, min(1,self.position.x / canvas_width))
        r = int(255 * ratio)
        b = int(255 * (1 - ratio))
        self.color =  (r, 0, b)
    
    @staticmethod
    def neighbor_check(current_ball, balls):
        neighbors = []
        totalweight = current_ball.social
        avgx, avgy = (current_ball.position[0] * current_ball.social), (current_ball.position[1] * current_ball.social)

        for ball in balls:
            if ball is not current_ball:
                dx = ball.position[0] - current_ball.position[0]
                dy = ball.position[1] - current_ball.position[1]
                distance = math.sqrt(dx**2 + dy**2)
                if distance <= config.NEIGHBOR_RADIUS:
                    #neighbors.append(ball)
                    avgx += (ball.position[0] * ball.social)
                    avgy += (ball.position[1] * ball.social)
                    totalweight += ball.social

        if totalweight == 0:
            current_ball.velocity = pygame.math.Vector2((0,0))
        elif totalweight > 0:
            avgx /= totalweight
            avgy /= totalweight
            dx = avgx - current_ball.position[0]
            dy = avgy - current_ball.position[1]
            current_ball.velocity = pygame.math.Vector2((dx, dy))

        return(neighbors)

    @classmethod
    def get_ball_count(cls):
        return f"Total # of balls: {cls.ballcount}"

