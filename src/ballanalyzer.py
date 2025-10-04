"""
Class: {file_name}
Author: MORS
Date: {date}

Description:
Tools to analyze items from the Ball Class

Usage:
This is used to analyze the results 

Future Items:
Look into replacing the "if not balls" with a wrapper function

"""
import math
import sys

import ball  # noqa: F401


class BallAnalyzer:

    @staticmethod
    def count_by_color(balls):
        if not balls:
            print("\033[91mSomething went wrong at initialization, ball list is empty.\033[0m")  # noqa: E501
            sys.exit()
        counts = {}
        for ballitem in balls:
            counts[ballitem.color] = counts.get(ballitem.color, 0) + 1
        return counts

    @staticmethod
    def count_by_speed_range(balls, thresholds):
        if not balls:
            print("\033[91mSomething went wrong at initialization, ball list is empty.\033[0m")  # noqa: E501
            sys.exit()
        # thresholds = [(0, 2), (2, 5), (5, 10)]
        counts = {rng: 0 for rng in thresholds}
        for ballitem in balls:
            s = ballitem.speed()
            for rng in thresholds:
                if rng[0] <= s < rng[1]:
                    counts[rng] += 1
                    break
        return counts

    @staticmethod
    def count_by_direction_sector(balls, sectors):
        if not balls:
            print("\033[91mSomething went wrong at initialization, ball list is empty.\033[0m")  # noqa: E501
            sys.exit()
        # sectors = [(0, 90), (90, 180), ...] in degrees
        counts = {rng: 0 for rng in sectors}
        for ballitem in balls:
            angle = math.degrees(ballitem.direction()) % 360
            for rng in sectors:
                if rng[0] <= angle < rng[1]:
                    counts[rng] += 1
                    break
        return counts
    
    @staticmethod
    def average_ball_color(balls):
        if not balls:
            print("\033[91mSomething went wrong at initialization, ball list is empty.\033[0m")  # noqa: E501
            sys.exit()

        num_balls = len(balls)
        r , g, b = 0,0,0

        for ballitem in balls:
            r += ballitem.color[0]
            g += ballitem.color[1]
            b += ballitem.color[2]

        color = (int(r/num_balls), int(g/num_balls), int(b/num_balls))
        return color
