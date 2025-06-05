choice = input("what would you like?(espresso/latte/cappuccino):")
is_machine_on = True
while is_machine_on:
    choice = input("what would you like?(espresso/latte/cappuccino):")
    if choice.lower()=="off":
        is_machine_on = False