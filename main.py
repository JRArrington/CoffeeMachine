import math
from data import menu
from data import resources

money = 0
espresso_cost = float(menu['espresso']['cost'])
latte_cost = float(menu['latte']['cost'])
cappuccino_cost = float(menu['cappuccino']['cost'])
refund = 0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']


# Check resources sufficient
def check_resources():
    if water < menu['espresso']['ingredients']['water'] or water < menu['latte']['ingredients']['water'] or water < \
            menu['cappuccino']['ingredients']['water']:
        print("Sorry, there is not enough water.")
        in_use()
    elif milk < menu['latte']['ingredients']['milk'] or milk < menu['cappuccino']['ingredients']['milk']:
        print("Sorry, there is not enough milk.")
    elif coffee < menu['espresso']['ingredients']['coffee'] or coffee < menu['latte']['ingredients'][
        'coffee'] or coffee < menu['cappuccino']['ingredients']['coffee']:
        print("Sorry, there is not enough coffee.")


# Print report
# Check user's input to decide what to do next.
def in_use():
    coffee_machine_on = True
    while coffee_machine_on == True:
        drink = input("What would you like? (espresso/latte/cappuccino): ")

        def process_coins():
            global money
            global water
            global milk
            global coffee

            penny = 0.01
            nickel = 0.05
            dime = 0.10
            quarter = 0.25

            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total = ((quarter * quarters) + (dime * dimes) + (nickel * nickels) + (penny * pennies))

            if drink == 'espresso':
                if total < espresso_cost:
                    print("Sorry, that's not enough money. Money refunded.")
                elif total == espresso_cost:
                    money = total + money
                    water = water - 50
                    coffee = coffee - 18
                    print("Here is your espresso. Enjoy!")
                elif total > espresso_cost:
                    refund = total - espresso_cost
                    money = money - refund
                    water = water - 50
                    coffee = coffee - 18
                    print(f"Here is ${math.ceil(refund * 100) / 100} dollars in change.")
                    print("Here is your espresso. Enjoy!")
            elif drink == 'latte':
                if total < latte_cost:
                    print("Sorry, that's not enough money. Money refunded.")
                elif total == latte_cost:
                    money = money + total
                    water = water - 200
                    milk = milk - 150
                    coffee = coffee - 24
                    print("Here is your latte. Enjoy!")
                elif total > latte_cost:
                    refund = total - latte_cost
                    money = money - refund
                    water = water - 200
                    milk = milk - 150
                    coffee = coffee - 24
                    print(f"Here is ${math.ceil(refund * 100) / 100} dollars in change.")
                    print("Here is your latte. Enjoy!")
            elif drink == 'cappuccino':
                if total < cappuccino_cost:
                    print("Sorry, that's not enough money. Money refunded")
                elif total == cappuccino_cost:
                    money = money + total
                    water = water - 250
                    milk = milk - 100
                    coffee = coffee - 24
                    print("Here is your cappuccino. Enjoy!")
                elif total > cappuccino_cost:
                    refund = total - cappuccino_cost
                    money = money - refund
                    water = water - 250
                    milk = milk - 100
                    coffee = coffee - 24
                    print(f"Here is ${math.ceil(refund * 100) / 100} dollars in change.")
                    print("Here is your cappuccino. Enjoy!")

        if drink == 'off':
            coffee_machine_on = False
        elif drink == 'report':
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
        elif drink == 'espresso':
            check_resources()
            process_coins()
        elif drink == 'latte':
            check_resources
            process_coins()
        elif drink == 'cappuccino':
            check_resources()
            process_coins()


in_use()
# Check transaction successful?
# Make Coffee
