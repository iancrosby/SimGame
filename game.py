__author__ = 'iwcrosby'

import pygame
from pygame.locals import *
from functions import *
from sales_screen import *
pygame.init()

import var

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
cpl = 0
advance_month = False

new_leads = 0
lost_prospects = 0
trials = 0
lost_trials = 0
customers = 0
churns = 0


#Initialize buttons
button_list = []
pressed = None

sales_btn = Button(120,15,(25,25),"Sales")
button_list.append(sales_btn)

next_month = Button(120,15,(400,75),"Next Month")
button_list.append(next_month)

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
        elif event.type == MOUSEBUTTONDOWN:
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
        if pressed == next_month:
            advance_month = True
        elif pressed == sales_btn:
            sales_screen(screen)
        elif pressed == mkt_button_up:
            pass
        elif pressed == mkt_button_down and dm_spend >= 1000:
            pass
        elif pressed == price_button_up:
            pass
        elif pressed == price_button_down and price >= 2:
            pass
        pressed = False #Pressed needs to be reset with MOUSEBUTTONUP before we will react to any more button events
    #End of button logic


    # ADVANCE MONTH, CALCULATE NEW VALUES
    if advance_month == True:

        #Existing customers change statuses
        for cust in var.customer_list:
            #Convert prospects
            if cust.status == 0:
                cust.conv_prospect()
                if cust.status == 1:
                    lost_prospects += 1
                elif cust.status == 2:
                    trials += 1
                else:
                    raise Exception

            #convert trials
            elif cust.status == 2:
                cust.conv_trial()
                if cust.status == 3:
                    lost_trials += 1
                    trials -= 1
                elif cust.status == 4:
                    customers += 1
                    trials -= 1
                else:
                    raise Exception

            elif cust.status == 4:
                cust.churn()
                if cust.status == 5:
                    churns += 1
                    customers -= 1
                else:
                    var.cash += cust.price


        #Add new prospects
        cpl = ((var.price1 * var.price1) / 500) + 50
        new_leads = var.adwords_spend / cpl
        add_customers = new_leads
        while add_customers > 0:
            Customer()
            add_customers -= 1

        var.cash -= var.adwords_spend + var.rd_spend

        var.month += 1
        advance_month = False


    # END OF ADVANCE MONTH CALCULATIONS


    # END OF GAME LOGIC


    #ALL GRAPHICS RENDERING OCCURS HERE
    screen.fill(white)


    #Set the font to draw text in
    font = pygame.font.Font(None, 20)

    #Define what text should be written
    cash_text = font.render("Cash = $" + str(var.cash),True,black)
    customer_text = font.render("Customers = " + str(customers),True,black)
    month_text = font.render("Month = "+str(var.month),True,black)
    #price_text = font.render("Price = $"+str(price),True,black)
    dm_spend_text = font.render("Direct marketing spend = $"+str(var.adwords_spend+var.rd_spend),True,black)
    cpl_text = font.render("Cost per lead = $"+str(cpl),True,black)
    new_leads_text = font.render("New leads = "+str(new_leads),True,black)
    trials_text = font.render("Trials = "+str(trials),True,black)
    churns_text = font.render("Churns = "+str(churns),True,black)
    all_entries_text = font.render("All entries = "+str(len(var.customer_list)),True,black)

    fps_text = font.render("FPS = "+str(clock.get_fps())[:4],True,black)

    #Write all text to screen
    screen.blit(month_text, (25, 75))
    screen.blit(cash_text, (25, 100))
    screen.blit(customer_text, (25, 125))
    #screen.blit(price_text, (25, 150))
    screen.blit(dm_spend_text, (25, 175))
    screen.blit(cpl_text, (25, 200))
    screen.blit(new_leads_text, (25, 225))
    screen.blit(trials_text, (25, 250))
    screen.blit(churns_text, (25, 275))
    screen.blit(all_entries_text, (25, 300))

    screen.blit(fps_text, (900, 700))

    #Draw button boxes and labels to screen
    for button in button_list:
        screen.blit(font.render(button.label,True,black), (button.rect.x+5,button.rect.y+1))
        pygame.draw.rect(screen, black, button.rect, 1)


    pygame.display.flip()
    # END OF GRAPHICS RENDERING

    clock.tick(30)
