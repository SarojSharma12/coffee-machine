from utils import get_resources_report, is_resources_sufficient, process_coins

is_machine_on = True

while is_machine_on:
    choice = input("what would you like?(espresso/latte/cappuccino): ")
    if choice.lower() == "off":
        is_machine_on = False

    elif choice.lower() == "report":
        get_resources_report()

    else:
        if choice not in ["latte","espresso","cappuccino"]:
            print(f"sorry!!!{choice} is not available. select correctly")
        else:
            if is_resources_sufficient(choice):
                process_coins(choice)
