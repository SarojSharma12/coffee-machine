from resources_db import machine_resources as resources
from resources_db import COFFEE_MENU
def get_resources_report():
    print(f"water:{resources.get('water',' ')}ml")
    print(f"milk:{resources.get('milk',' ')}ml")
    print(f"coffee:{resources.get('coffee',' ')}gm")
    print(f"money:{resources.get('money',' ')}")

def is_resources_sufficient(choice):
    is_resources_suff = True
    for ingred, qty in COFFEE_MENU.get(choice,{}).get("ingredients", {}).items():
        if resources.get(ingred, 0) < qty:
            print(f"we dont have enough{ingred}!!! Try another coffee.")
            is_resources_sufficient = False
            break

    return is_resources_suff
    
def process_coins(choice):
    print(" Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?:"))
    nickles = int(input("how many nickles?:"))
    pennies = int(input("how many pennies?:"))
      
    total =  0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    cost = COFFEE_MENU.get(choice,{}).get("money"," ")
    

    if total>cost: 
        print(f"Here is ${round(total - cost, 2)} in change 💰.")
        print(f"here is your {choice}🍵 .Enjoy!")

    if "money" in resources and isinstance(resources.get("money"," "),(float,int)):
        resources["money"] += cost
    else:
         print("KEYERROR !!! 'money' is not found as key in resources.")
    for ingred, qty in COFFEE_MENU.get(choice,{}).get("ingredients",{}).items():
        resources[ingred] -= qty
    else:
        print("Sorry that's not enough money. Money refunded.")
     

