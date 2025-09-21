"""
Class: {file_name}
Author: MORS
Date: {date}

Description:
{brief_description_of_the_file}

Usage:
{brief_usage_instructions}

"""
import math

import ball  # noqa: F401


class BallAnalyzer:
    def count_by_color(balls):
        counts = {}
        for ballitem in balls:
            counts[ballitem.color] = counts.get(ballitem.color, 0) + 1
        return counts

    def count_by_speed_range(balls, thresholds):
        # thresholds = [(0, 2), (2, 5), (5, 10)]
        counts = {rng: 0 for rng in thresholds}
        for ballitem in balls:
            s = ballitem.speed()
            for rng in thresholds:
                if rng[0] <= s < rng[1]:
                    counts[rng] += 1
                    break
        return counts

    def count_by_direction_sector(balls, sectors):
        # sectors = [(0, 90), (90, 180), ...] in degrees
        counts = {rng: 0 for rng in sectors}
        for ballitem in balls:
            angle = math.degrees(ballitem.direction()) % 360
            for rng in sectors:
                if rng[0] <= angle < rng[1]:
                    counts[rng] += 1
                    break
        return counts
