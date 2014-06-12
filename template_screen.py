__author__ = 'iwcrosby'

import pygame
from pygame.locals import *
from functions import *


def template_screen(screen):
    #Initialize engine stuff
    done=False
    pygame.display.set_caption("SimGame")
    clock=pygame.time.Clock()

    #Define colours for easy use later
    black    = (   0,   0,   0)
    white    = ( 255, 255, 255)
    green    = (   0, 255,   0)
    red      = ( 255,   0,   0)
    blue     = (   0,   0, 255)
    d_grey   = (  60,  60,  60)

    #Initialize buttons
    button_list = []
    pressed = None

    back = Button(120,15,(25,25),"Back")
    button_list.append(back)

    button1 = Button(120,15,(25,50),"button1")
    button_list.append(button1)

    button2 = Button(120,15,(25,75),"button2")
    button_list.append(button2)

    button3 = Button(120,15,(25,100),"button3")
    button_list.append(button3)

    button4 = Button(120,15,(25,125),"button4")
    button_list.append(button4)
    #End of button initialization


    # -------- Main Program Loop -----------
    while done==False:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT

        #Reset to basic state


        for event in pygame.event.get(): # User did something
            if event.type == QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and pressed == None:
                    for button in button_list:
                        if button.rect.collidepoint(event.pos):
                            pressed = button
            elif event.type == MOUSEBUTTONUP:
                pressed = None #Reset button status when user releases mouse button

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        #Button logic goes here
        if pressed <> None:
            if pressed == back:
                done=True
            elif pressed == button1:
                pass
            elif pressed == button2:
                pass
            elif pressed == button3:
                pass
            elif pressed == button4:
                pass

            pressed = False #Pressed needs to be reset with MOUSEBUTTONUP before we will react to any more button events
            #End of button logic



        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.fill(white)

        #Set the font to draw text in
        font = pygame.font.Font(None, 20)

        for button in button_list:
            screen.blit(font.render(button.label,True,black), (button.rect.x+5,button.rect.y+1))
            pygame.draw.rect(screen, black, button.rect, 1)


        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        pygame.display.flip()
