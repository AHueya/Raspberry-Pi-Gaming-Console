#-------------------------------------------------------------------------------------
# CpE 185 - Final Project: Raspberry Pi Game Code
#
# Andersen Huey
#
# Lecture: Dennis Dahlquist
# Lab: Eric Telles
#
# This program will display a GUI along with some text
#-------------------------------------------------------------------------------------

# Import pygame library
import pygame
from pygame.locals import *

def main():

    # Initialize screen/GUI
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('CpE 185 - Final Project')

    # Initialize font
    font = pygame.font.Font(None, 36)

    # Initialize colors
    BLACK = (10, 10, 10)
    WHITE = (250, 250, 250)

    # Initalize background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    # Initialize text position
    text = font.render('Counter', 1, BLACK)
    textPos = text.get_rect()
    textPos.centerx = screen.get_rect().centerx
    textPos.centery = screen.get_rect().centery - 100

    # Initialize counter and counter position
    counter = 0
    counterDisplay = font.render(str(counter), 1, BLACK)
    counterPos = counterDisplay.get_rect()
    counterPos.centerx = screen.get_rect().centerx
    counterPos.centery = screen.get_rect().centery

    # Block Image Transfer (Blit) to screen
    screen.blit(background, (0, 0))
    screen.blit(text, textPos)
    screen.blit(counterDisplay, counterPos)
    pygame.display.flip()

    # Infinite loop
    while 1:

        # Event loop - waits for some event to run
        for event in pygame.event.get():

            # If the quit button is pressed, end program
            if event.type == QUIT:
                return

if __name__ == '__main__': main()
