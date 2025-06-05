from resources_db import machine_resources as resources
def get_resources_report():
    print(f"water:{resources.get('water',' ')}ml")
    print(f"milk:{resources.get('water',' ')}ml")
    print(f"coffee:{resources.get('water',' ')}gm")
    print(f"money:{resources.get('water',' ')}ml")

is_machine_on = True
while is_machine_on:
    choice = input("what would you like?(espresso/latte/cappuccino):")
    if choice.lower()=="off":
        is_machine_on = False

    elif choice.lower() == "report":
        get_resources_report()