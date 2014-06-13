__author__ = 'iwcrosby'

import pygame
from pygame.locals import *
from functions import *
from sales_screen import *
pygame.init()

#Setting up some initialization stuff
done=False
scr_size = [1024,768]
screen=pygame.display.set_mode(scr_size)
pygame.display.set_caption("SimGame")
clock=pygame.time.Clock()

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

sales_btn = Button(120,15,(25,25),"Sales")
button_list.append(sales_btn)

next_week = Button(120,15,(400,75),"Next Week")
button_list.append(next_week)

price_button_up = Button(120,15,(400,150),"Increase")
button_list.append(price_button_up)

price_button_down = Button(120,15,(550,150),"Decrease")
button_list.append(price_button_down)

mkt_button_up = Button(120,15,(400,175),"Increase")
button_list.append(mkt_button_up)

mkt_button_down = Button(120,15,(550,175),"Decrease")
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


    #Button logic goes here
    if pressed <> None:
        if pressed == next_week:
            advance_week = True
        elif pressed == sales_btn:
            sales_screen(screen)
        elif pressed == mkt_button_up:
            dm_spend += 1000
        elif pressed == mkt_button_down and dm_spend >= 1000:
            dm_spend -= 1000
        elif pressed == price_button_up:
            price += 1
        elif pressed == price_button_down and price >= 2:
            price -= 1
        pressed = False #Pressed needs to be reset with MOUSEBUTTONUP before we will react to any more button events
    #End of button logic


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
    font = pygame.font.Font(None, 20)

    #Define what text should be written
    cash_text = font.render("Cash = $" + str(cash),True,black)
    customer_text = font.render("Customers = " + str(customers),True,black)
    week_text = font.render("Week = "+str(week),True,black)
    price_text = font.render("Price = $"+str(price),True,black)
    dm_spend_text = font.render("Direct marketing spend = $"+str(dm_spend),True,black)
    cac_text = font.render("CAC = $"+str(cac),True,black)

    fps_text = font.render("FPS = "+str(clock.get_fps()),True,black)

    #Write all text to screen
    screen.blit(week_text, (25, 75))
    screen.blit(cash_text, (25, 100))
    screen.blit(customer_text, (25, 125))
    screen.blit(price_text, (25, 150))
    screen.blit(dm_spend_text, (25, 175))
    screen.blit(cac_text, (25, 200))

    screen.blit(fps_text, (900, 700))

    #Draw button boxes and labels to screen
    for button in button_list:
        screen.blit(font.render(button.label,True,black), (button.rect.x+5,button.rect.y+1))
        pygame.draw.rect(screen, black, button.rect, 1)


    pygame.display.flip()
    # END OF GRAPHICS RENDERING

    clock.tick(30)
