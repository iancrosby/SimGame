__author__ = 'iwcrosby'

import pygame
from pygame.locals import *
from functions import *
from pricing_screen import *
from advertising_screen import *

import var

def sales_screen(screen):
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

    sales_team = Button(120,15,(25,50),"Sales Team")
    button_list.append(sales_team)

    advertising = Button(120,15,(25,75),"Advertising")
    button_list.append(advertising)

    pricing = Button(120,15,(25,100),"Pricing")
    button_list.append(pricing)

    content = Button(120,15,(25,125),"Content")
    button_list.append(content)
    #End of button initialization

    #Calculate stats

    lost_leads = 0.0
    trials = 0.0
    lost_trials = 0.0
    all_customers = 0.0
    customers = 0.0
    churns = 0.0
    lead_trial_rate = 0.0
    trial_cust_rate = 0.0
    churn_rate = 0.0


    for cust in var.customer_list:
        if cust.status == 1:
            if cust.lost_lead_date == var.month - 1:
                lost_leads += 1
        elif cust.status == 2:
            if cust.trial_date == var.month - 1:
                trials += 1
        elif cust.status == 3:
            if cust.lost_trial_date == var.month - 1:
                lost_trials += 1
        elif cust.status == 4:
            all_customers += 1
            if cust.cust_date == var.month - 1:
                customers += 1
        elif cust.status == 5:
            if cust.churn_date == var.month - 1:
                churns += 1

    if trials > 0:
        lead_trial_rate = trials / (lost_leads + trials)

    if customers > 0:
        trial_cust_rate = customers / (customers + lost_trials)

    if churns > 0:
        churn_rate = churns / all_customers




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
            if pressed == back:
                done=True
            elif pressed == sales_team:
                pass
            elif pressed == advertising:
                advertising_screen(screen)
            elif pressed == pricing:
                pricing_screen(screen)
            elif pressed == content:
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

        #Define what text should be written
        lead_trial_text = font.render("Lead-Trial conversion = " + str(lead_trial_rate*100)[:4] + "%",True,black)
        trial_cust_text = font.render("Trial-Cust conversion = " + str(trial_cust_rate*100)[:4] + "%",True,black)
        churn_text = font.render("Churn = " + str(churn_rate*100)[:4] + "%",True,black)

        #Write all text to screen
        screen.blit(lead_trial_text, (300, 50))
        screen.blit(trial_cust_text, (300, 75))
        screen.blit(churn_text, (300, 100))



        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        pygame.display.flip()
