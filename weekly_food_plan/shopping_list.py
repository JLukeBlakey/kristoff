#!/usr/bin/python3

import yaml
import random 
import smtplib
from email.message import EmailMessage

meals = []
shopping_list = {}
recipes = yaml.safe_load(open("recipes.yaml"))
regulars = open("regulars.txt")
recipients = ["luke.blakey@gmail.com"]#, "hmjstath@gmail.com"]
kristoff_open = "Bonjour, Kristoff here. Here's your shopping plan for this week:\n"

def create_meal_plan():
    while len(meals) != 5:
        random_meal = random.choice(list(recipes))
        #if random_meal not in dinners:
            #dinners.append(random_meal)
        meals.append(random_meal)
    schedule = "\nMonday: " +  meals[0] + "\nTuesday: " + meals[1] + "\nWednesday: " + meals[2] + "\nThursday: " + meals[3] + "\nFriday: " + meals[4]
    return schedule    
    

def create_shopping_list(meals):
    for meal in meals:
        for ingredient, quantity in recipes[meal].items():
            if ingredient in shopping_list and shopping_list[ingredient][1] == quantity[1]:
                shopping_list[ingredient][0] = shopping_list[ingredient][0] + quantity[0]
            else:
                shopping_list[ingredient] = []
                shopping_list[ingredient].append(quantity[0])
                shopping_list[ingredient].append(quantity[1])
    return shopping_list

  #  for k, v in shopping_list.items():
  #      print(k, v)
  #      
  #      lists = (str(k) + ':' + str(v[0]) + str(v[1]))
  #  
  #  print(lists)

    #return lists


def email(content):
    for address in recipients:
        msg = EmailMessage()
        msg.set_content(content)
        msg["Subject"] = "Weekly Shop"
        msg["From"] = "Kristoff"
        msg["To"] = address
        mail = smtplib.SMTP("localhost")
        mail.send_message(msg)
        mail.quit


#create_meal_plan()
###print(meals['Chilli']['ingredients']['item'])
##create_shopping_list(meals)
#listss = create_shopping_list(meals)
#€print(listss)
#
#for k, v in list.items():
#    content=print(k, ':', v[0], v[1])
#print(content)

#dic={}
#for k, v in recipes['Chilli']['ingredients'].items():
# #   print(k)
#  #  print(v)
#    dic[k]=v['quantity']
#print(dic)
#for k, v in recipes['Chilli']['ingredients'].items():
##    print(k)
# #   print(v)
#    if k in dic:
#        dic[k]=dic[k] + v['quantity']
#    else:
#        dic[k]=v['quantity']
#

#print(dic)

content = kristoff_open + create_meal_plan() + "\n\nBuy these things:\n" + str(create_shopping_list(meals)) + "Don't forget the regulars!\n" + regulars.read() + "\nKristoff out."
print(content)
#email(content)
