# COFFEE MACHINE
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_made = 0
water_left = resources["water"]
coffee_left = resources["coffee"]
milk_left = resources["milk"]

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def report():
    """Prints report that shows remaining resources and money made"""
    print(f"Money: ${money_made}")
    print(f"Water: {water_left}ml")
    print(f"Coffee: {coffee_left}g")
    print(f"Milk: {milk_left}ml")


def coins_count():
    """Adds up value of coins inserted and returns total amount."""
    amount_inserted = (num_quarters * QUARTER) + (num_dimes * DIME) + (num_nickels * NICKEL) + (num_pennies * PENNY)
    return amount_inserted


def is_resources_sufficient(drink):
    """Checks whether there are sufficient ingredients to make the drink.
    Returns False if resources are insufficient and True if resources are sufficient."""
    if water_left < MENU[drink]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif coffee_left < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        return False
    elif drink == "latte" or drink == "cappuccino":
        if milk_left < MENU[drink]["ingredients"]["milk"]:
            print("Sorry, there is not enough coffee.")
            return False
    return True


def is_funds_sufficient(drink):
    """Checks whether the total value of the coins received is sufficient to purchase the drink.
    Returns False if funds are insufficient and True if funds are sufficient."""
    # print(round(coins_count(), 2))  # test code
    # print(MENU[drink]["cost"])  # test code
    if coins_count() < MENU[drink]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif coins_count() > MENU[drink]["cost"]:
        return True
    return True


coffee_machine_is_on = True
while coffee_machine_is_on:

    # User prompt
    response = input("What drink would you like? (espresso $1.50 / latte $2.50 / cappuccino $3.00): ").lower()

    # Turn off the coffee machine. Prompt is "off".
    # Print report that shows current values of [Water, Milk, Coffee, Money]. Prompt is "report".
    # Check resources sufficient.
    if response == "off":
        coffee_machine_is_on = False
    elif response == "report":
        report()
    elif response == "espresso" or response == "latte" or response == "cappuccino":
        # Check that resources are sufficient
        if is_resources_sufficient(drink=response):
            # Process coins and check that funds are sufficient.
            print("Please insert coins.")
            num_quarters = int(input("How many quarters?: "))
            num_dimes = int(input("How many dimes?: "))
            num_nickels = int(input("How many nickels?: "))
            num_pennies = int(input("How many pennies?: "))

            # Check that funds are sufficient
            if is_funds_sufficient(drink=response):
                change = coins_count() - MENU[response]["cost"]
                print(f"Here is ${round(change, 2)} in change.")
                print(f"Here is your {response} ☕. Enjoy!")

                # Update report
                money_made += MENU[response]["cost"]
                water_left -= MENU[response]["ingredients"]["water"]
                coffee_left -= MENU[response]["ingredients"]["coffee"]
                if response == "latte" or response == "cappuccino":
                    milk_left -= MENU[response]["ingredients"]["milk"]
    else:
        print("Invalid response. Try again")
