__author__ = 'iwcrosby'

import pygame
from pygame.locals import *
from functions import *
pygame.init()

#Setting up some initialization stuff
done=False
scr_size = [1024,768]
screen=pygame.display.set_mode(scr_size)
pygame.display.set_caption("SquadGame")
clock=pygame.time.Clock()

clock = pygame.time.Clock()

#Define colours for easy use later
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
d_grey   = (  60,  60,  60)

#Initialize some defaults
customers = 0
cash = 0
week = 1

#Initialize buttons
button_list = []
pressed = None

mkt_button_up = button(80,15,(500,20),"Increase")
button_list.append(mkt_button_up)

mkt_button_down = button(80,15,(500,40),"Decrease")
button_list.append(mkt_button_down)

next_week = button(80,15,(500,60),"Next Week")
button_list.append(next_week)






# -------- Main Program Loop -----------
while done==False:
# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT

#Reset to basic state

    for event in pygame.event.get(): # User did something
        if event.type == QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
            for button in button_list:
                if button.rect.collidepoint(event.pos):
                    pressed = button


    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    if pressed == mkt_button_up:
        customers += 1
    elif pressed == mkt_button_down:
        customers -= 1
    elif pressed == next_week:
        week += 1

    pressed = None #reset button status



    # END OF GAME LOGIC


    #ALL GRAPHICS RENDERING OCCURS HERE
    screen.fill(white)

    #Set the font to draw text in
    font = pygame.font.Font(None, 25)

    #Define what text should be written
    cash_text = font.render("Cash = $" + str(cash),True,black)
    customer_text = font.render("Customers = " + str(customers),True,black)
    week_text = font.render("Week = "+str(week),True,black)

    fps_text = font.render("FPS = "+str(clock.get_fps()),True,black)

    #Write all text to screen
    screen.blit(cash_text, (20, 20))
    screen.blit(customer_text, (20, 40))
    screen.blit(week_text, (20, 60))

    screen.blit(fps_text, (900, 700))

    #Write all button labels to screen
    for button in button_list:
        screen.blit(font.render(button.label,True,black), (button.rect.x, button.rect.y))


    pygame.display.flip()
    # END OF GRAPHICS RENDERING

    clock.tick(30)
