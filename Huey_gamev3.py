#-------------------------------------------------------------------------------------
# CpE 185 - Final Project: Raspberry Pi Game Code
#
# Andersen Huey
#
# Lecture: Dennis Dahlquist
# Lab: Eric Telles
#
# This program will display a GUI with a counter that will increment when 'a' is
# pressed and decrement when 'l' is pressed.
#
# Two controllers with two buttons can also be connected via USB to play the game
#-------------------------------------------------------------------------------------

# Import pygame library
import pygame
from pygame.locals import *

# Import Serial library
import serial

def main():
    serialport = serial.Serial('/dev/ttyACM0', 9600, timeout = 0.5)
    serialport2 = serial.Serial('/dev/ttyACM1', 9600, timeout = 0.5)

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

        command = serialport.read()
        command2 = serialport2.read()

        if (command == '1' or command2 == '1'):

            if(command == '1'):
                counter += 1

            if(command2 == '1'):
                counter -= 1

            counterDisplay = font.render(str(counter), 1, BLACK)
            screen.blit(background, (0,0))
            screen.blit(text, textPos)
            screen.blit(counterDisplay, counterPos)
            pygame.display.flip()

        elif (command == '2' or command2 == '2'):
            return

        if (counter >= 20 or counter <= -20):
            if (counter >= 20):
                text = font.render('Player 1 Wins', 1, BLACK)
            if (counter <= -20):
                text = font.render('Player 2 Wins', 1, BLACK)

            textPos = text.get_rect()
            textPos.centerx = screen.get_rect().centerx
            textPos.centery = screen.get_rect().centery - 100
            screen.blit(background, (0,0))
            screen.blit(text, textPos)
            pygame.display.flip()

            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        return


        # Event loop - waits for some event to run
        for event in pygame.event.get():

            # If the quit button is pressed, end program
            if event.type == QUIT:
                return

            # If a key is pressed
            if event.type == pygame.KEYDOWN:

                # if 'a' is pressed, increment 1
                if event.key == pygame.K_a:
                    counter += 1
                    counterDisplay = font.render(str(counter), 1, BLACK)

                # if 'l' is pressed, decrement 1
                if event.key == pygame.K_l:
                    counter -= 1
                    counterDisplay = font.render(str(counter), 1, BLACK)

                # Refresh the screen
                screen.blit(background, (0, 0))
                screen.blit(text, textPos)
                screen.blit(counterDisplay, counterPos)

                pygame.display.flip()

if __name__ == '__main__': main()
