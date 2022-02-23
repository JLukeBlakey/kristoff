#!/usr/bin/python3

import yaml
import random 
import smtplib
from email.message import EmailMessage

dinners = []
shopping_list = []
meals = yaml.load(open("meals.yaml"), Loader=yaml.BaseLoader)
regulars = open("regulars.txt")
recipients = ["luke.blakey@gmail.com", "hmjstath@gmail.com"]
Kristoff_open = "Bonjour, Kristoff here. Here's your shopping plan for this week:\n"

def create_schedule():
    while len(dinners) != 5:
        random_meal = random.choice(list(meals))
        if random_meal not in dinners:
            dinners.append(random_meal)
    schedule = "\nMonday: " +  dinners[0] + "\nTuesday: " + dinners[1] + "\nWednesday: " + dinners[2] + "\nThursday: " + dinners[3] + "\nFriday: " + dinners[4]
    return schedule    
    

def create_shopping_list(dinners):
    list_initial = []
    for meal in dinners:
        list_initial.append(meals[meal])

    list_flat = []
    for meal in list_initial:  
        for ingredient in meal:    
            list_flat.append(ingredient)

    list_dict = {}
    for item in set(list_flat):
        list_dict[item] = 0
    for item in list_flat:
        list_dict[item] += 1
    for key in list_dict:
        if list_dict[key] == 1:
            shopping_list.append(key)
        else:
            shopping_list.append("{}({})".format(key, list_dict[key]))
    return ", ".join(shopping_list) + "\n\n"


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


content = Kristoff_open + create_schedule() + "\n\nBuy these things:\n" + create_shopping_list(dinners) + "Don't forget the regulars!\n" + regulars.read() + "\nKristoff out."
email(content)
