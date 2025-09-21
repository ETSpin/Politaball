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
    import pygame
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Politaball")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((30, 30, 30))
        pygame.display.flip()
    pygame.quit()



if __name__ == '__main__':
    main()
