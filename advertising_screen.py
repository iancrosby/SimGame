__author__ = 'iwcrosby'

import pygame
from pygame.locals import *
from functions import *


def advertising_screen(screen):
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

    #Initialize variables
    adwords_spend = 20000
    rd_spend = 5000


    #Initialize buttons
    button_list = []
    pressed = None

    back = Button(120,15,(25,25),"Back")
    button_list.append(back)

    adwords_up = Button(30,15,(200,75),"  +  ")
    button_list.append(adwords_up)

    adwords_down = Button(30,15,(230,75),"  -  ")
    button_list.append(adwords_down)

    rd_up = Button(30,15,(200,100),"  +  ")
    button_list.append(rd_up)

    rd_down = Button(30,15,(230,100),"  -  ")
    button_list.append(rd_down)
    #End of button initialization


    # -------- Main Program Loop -----------
    while done==False:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT


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
            elif pressed == adwords_up:
                adwords_spend += 5000
            elif pressed == adwords_down and adwords_spend >= 5000:
                adwords_spend -= 5000
            elif pressed == rd_up:
                rd_spend += 5000
            elif pressed == rd_down and rd_spend >= 5000:
                rd_spend -= 5000

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

        #Define what text should be written
        title_text = font.render("Advertising projects",True,black)
        adwords_text = font.render("Adwords spend = $" + str(adwords_spend),True,black)
        rd_text = font.render("R&D spend = $"+str(rd_spend),True,black)

        #Write all text to screen
        screen.blit(title_text, (25, 50))
        screen.blit(adwords_text, (25, 75))
        screen.blit(rd_text, (25, 100))



        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        pygame.display.flip()

