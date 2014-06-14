__author__ = 'iwcrosby'

import pygame
from pygame.locals import *
from functions import *
import var

def pricing_screen(screen):
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

    price1_up = Button(30,15,(200,75),"  +  ")
    button_list.append(price1_up)

    price1_down = Button(30,15,(230,75),"  -  ")
    button_list.append(price1_down)

    limit1_up = Button(30,15,(200,100),"  +  ")
    button_list.append(limit1_up)

    limit1_down = Button(30,15,(230,100),"  -  ")
    button_list.append(limit1_down)

    price2_up = Button(30,15,(200,175),"  +  ")
    button_list.append(price2_up)

    price2_down = Button(30,15,(230,175),"  -  ")
    button_list.append(price2_down)

    limit2_up = Button(30,15,(200,200),"  +  ")
    button_list.append(limit2_up)

    limit2_down = Button(30,15,(230,200),"  -  ")
    button_list.append(limit2_down)

    price3_up = Button(30,15,(200,275),"  +  ")
    button_list.append(price3_up)

    price3_down = Button(30,15,(230,275),"  -  ")
    button_list.append(price3_down)

    limit3_up = Button(30,15,(200,300),"  +  ")
    button_list.append(limit3_up)

    limit3_down = Button(30,15,(230,300),"  -  ")
    button_list.append(limit3_down)
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
            elif pressed == price1_up and var.price1 <= var.price2-10:
                var.price1 += 5
            elif pressed == price1_down and var.price1 >= 5:
                var.price1 -= 5
            elif pressed == limit1_up and var.limit1 <= var.limit2-2000:
                var.limit1 += 1000
            elif pressed ==limit1_down and var.limit1 >= 1000:
                var.limit1 -= 1000
            elif pressed == price2_up and var.price2 <= var.price3-10:
                var.price2 += 5
            elif pressed == price2_down and var.price2 >= (var.price1+10):
                var.price2 -= 5
            elif pressed == limit2_up and var.limit2 <= var.limit3-10000:
                var.limit2 += 1000
            elif pressed ==limit2_down and var.limit2 >= var.limit1+2000:
                var.limit2 -= 1000
            elif pressed == price3_up:
                var.price3 += 5
            elif pressed == price3_down and var.price3 >= var.price2+10:
                var.price3 -= 5
            elif pressed == limit3_up:
                var.limit3 += 5000
            elif pressed ==limit3_down and var.limit3 >= var.limit2+10000:
                var.limit3 -= 5000

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
        package1_text = font.render("Starter package",True,black)
        price1_text = font.render("Price = $" + str(var.price1),True,black)
        limit1_text = font.render("Expense limit = $"+str(var.limit1),True,black)

        package2_text = font.render("Team package",True,black)
        price2_text = font.render("Price = $" + str(var.price2),True,black)
        limit2_text = font.render("Expense limit = $"+str(var.limit2),True,black)

        package3_text = font.render("Business package",True,black)
        price3_text = font.render("Price = $" + str(var.price3),True,black)
        limit3_text = font.render("Expense limit = $"+str(var.limit3),True,black)

        #Write all text to screen
        screen.blit(package1_text, (25, 50))
        screen.blit(price1_text, (25, 75))
        screen.blit(limit1_text, (25, 100))

        screen.blit(package2_text, (25, 150))
        screen.blit(price2_text, (25, 175))
        screen.blit(limit2_text, (25, 200))

        screen.blit(package3_text, (25, 250))
        screen.blit(price3_text, (25, 275))
        screen.blit(limit3_text, (25, 300))



        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        pygame.display.flip()
