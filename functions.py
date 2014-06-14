__author__ = 'iwcrosby'

import pygame
from random import randrange
import var

class Button:
    '''A clickable button. Coordinate tuple p is the location. w and h are the width and height.'''

    def __init__(self, w=1, h=1, p=(0,0), label="no label"):

        self.rect = pygame.Rect(p,(w,h))
        self.label = label

class Customer:
    '''A customer.'''

    def __init__(self):
        self.status = 0
        x = randrange(0,100)
        self.size = x * x * 5
        self.price_sens = (x * 3.5) / randrange(1,3)
        var.customer_list.append(self)
        self.signup_date = var.month

    # 0 -> prospect
    # 1 -> lost prospect
    # 2 -> trial
    # 3 -> lost trial
    # 4 -> customer
    # 5 -> churn


    def conv_prospect(self):

        size = self.size
        price_sens = self.price_sens

        if size <= var.limit3:
            if size <= var.limit2:
                if size <= var.limit1:
                    price = var.price1
                else:
                    price = var.price2
            else:
                price = var.price3
        else:
            self.status = 1
            self.lost_lead_date = var.month

        if price < price_sens:
            self.price = price
            self.status = 2
            self.trial_date = var.month

        else:
            self.status = 1
            self.lost_lead_date = var.month

    def conv_trial(self):

        x = randrange(0,10)
        if x >= 4:
            self.status = 4
            self.cust_date = var.month
        else:
            self.status = 3
            self.lost_trial_date = var.month

    def churn(self):

        x = randrange(0,100)
        if x >= 98:
            self.status = 5
            self.churn_date = var.month

