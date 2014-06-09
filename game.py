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
cac = 0
cash = 100000
week = 1
price = 100
dm_spend = 10000
advance_week = False

#Initialize buttons
button_list = []
pressed = None

next_week = button(80,15,(400,25),"Next Week")
button_list.append(next_week)

price_button_up = button(80,15,(400,100),"Increase")
button_list.append(price_button_up)

price_button_down = button(80,15,(500,100),"Decrease")
button_list.append(price_button_down)

mkt_button_up = button(80,15,(400,125),"Increase")
button_list.append(mkt_button_up)

mkt_button_down = button(80,15,(500,125),"Decrease")
button_list.append(mkt_button_down)










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

    if pressed <> None:
        if pressed == next_week:
            advance_week = True
        elif pressed == mkt_button_up:
            dm_spend += 1000
        elif pressed == mkt_button_down and dm_spend >= 1000:
            dm_spend -= 1000
        elif pressed == price_button_up:
            price += 1
        elif pressed == price_button_down and price >= 2:
            price -= 1

        pressed = False #Pressed needs to be reset with MOUSEBUTTONUP before we will react to any more button events


    # ADVANCE WEEK, CALCULATE NEW VALUES
    if advance_week == True:
        cac = ((price * price * price) / 5000) + (price) + 400
        customers += dm_spend / cac
        cash += (customers * price) - (dm_spend)

        week += 1
        advance_week = False


    # END OF ADVANCE WEEK CALCULATIONS


    # END OF GAME LOGIC


    #ALL GRAPHICS RENDERING OCCURS HERE
    screen.fill(white)

    #Set the font to draw text in
    font = pygame.font.Font(None, 25)

    #Define what text should be written
    cash_text = font.render("Cash = $" + str(cash),True,black)
    customer_text = font.render("Customers = " + str(customers),True,black)
    week_text = font.render("Week = "+str(week),True,black)
    price_text = font.render("Price = $"+str(price),True,black)
    dm_spend_text = font.render("Direct marketing spend = $"+str(dm_spend),True,black)
    cac_text = font.render("CAC = $"+str(cac),True,black)

    fps_text = font.render("FPS = "+str(clock.get_fps()),True,black)

    #Write all text to screen
    screen.blit(week_text, (25, 25))
    screen.blit(cash_text, (25, 50))
    screen.blit(customer_text, (25, 75))
    screen.blit(price_text, (25, 100))
    screen.blit(dm_spend_text, (25, 125))
    screen.blit(cac_text, (25, 150))

    screen.blit(fps_text, (900, 700))

    #Write all button labels to screen
    for button in button_list:
        screen.blit(font.render(button.label,True,black), (button.rect.x, button.rect.y))


    pygame.display.flip()
    # END OF GRAPHICS RENDERING

    clock.tick(30)
