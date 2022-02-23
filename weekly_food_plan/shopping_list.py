#!/usr/bin/python3

import yaml
import random 
import smtplib

from email.message import EmailMessage

shopping_list = []
shopping_list_flat = []
#final = []
dinners = []
meals = yaml.load(open("meals.yaml"), Loader=yaml.BaseLoader)
regular_items = ["cheese", "crackers", "milk", "spinach", "berries", "yoghurt", "nuts", "apples", "lemon", "lime"]
regulars = "Don't forget the regulars!\n" + ", ".join(regular_items) + "\n\n"
Kristoff = "Bonjour, Kristoff here. Here's your shopping plan for this week:\n"
recipients = ["luke.blakey@gmail.com", "hmjstath@gmail.com"]

def create_schedule():
    while len(dinners) != 5:
        random_meal = random.choice(list(meals))
        if random_meal not in dinners:
            dinners.append(random_meal)
    schedule = "\nMonday: " +  dinners[0] + "\nTuesday: " + dinners[1] + "\nWednesday: " + dinners[2] + "\nThursday: " + dinners[3] + "\nFriday: " + dinners[4]
    return schedule    
    
def create_shopping_list():
    for meal in dinners:
        shopping_list.append(meals[meal])

    for meal in shopping_list:  
        for ingredient in meal:    
            shopping_list_flat.append(ingredient)

    shopping_list_flat.sort()
    shopping_list_string = ", ".join(shopping_list_flat) + "\n\n"
    return shopping_list_string
        
#def agg():
#    for i in shopping_list_flat:
#        if shopping_list_flat.count(i) > 1:
#            final.append(i + "(" + str(shopping_list_flat.count(i)) + ")")
#            #shopping_list_flat.remove(i)
#        final.append(i)
#    final.sort()

def email(content, to):
    for address in to:
        msg = EmailMessage()
        msg.set_content(content)
        msg["Subject"] = "Weekly Shop"
        msg["From"] = "Kristoff"
        msg["To"] = address
        mail = smtplib.SMTP("localhost")
        mail.send_message(msg)
        mail.quit

content = Kristoff + create_schedule() + "\n\nBuy these things:\n" + create_shopping_list() + regulars + "Kristoff out."
email(content, recipients)
