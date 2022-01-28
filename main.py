from resources import MENU
from resources import resources

# show prompt message for entering type of coffee
type_of_coffee = ''

is_off = False


# count the total money provided to machine
def count_money():
    quarters = int(input("How many quarters?")) * 0.25
    dimes = int(input("How many dimes?")) * 0.10
    nickles = int(input("How many quarters?")) * 0.05
    pennies = int(input("How many quarters?")) * 0.01
    return quarters + dimes + nickles + pennies


# for checking resources left in coffes machine
def is_enough_resource(types):
    """
    :param types: type of coffee insterde
    :return: True
    """
    match types:

        case 'espresso':
            espresso_require = MENU["espresso"]
            if espresso_require["ingredients"]["water"] > resources["water"]:
                print("Not Enough Water")
            elif espresso_require["ingredients"]["coffee"] > resources["coffee"]:
                print("Not Enough Coffee")
            else:
                total_money = count_money()
                if total_money >= espresso_require["cost"]:
                    print("Your Coffee")
                    resources["water"] = resources["water"] - espresso_require["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - espresso_require["ingredients"]["coffee"]
                    resources["Money"] = resources["Money"] + espresso_require["cost"]
                    if total_money > espresso_require["cost"]:
                        print(f"Please take your change: {round(total_money - espresso_require['cost'], 2 )}")
                else:
                    print("Sorry Don't have enough Money! Please Take your refunds")

        case 'latte':
            latte_require = MENU['latte']
            if latte_require["ingredients"]["water"] > resources["water"] :
                print("Not Enough Water")
            elif latte_require["ingredients"]["coffee"] > resources["coffee"]:
                print("Not Enough Coffee")
            elif latte_require["ingredients"]["milk"] > resources["milk"]:
                print("Not Enough coffee")
            else:
                total_money = count_money()
                print(f"total money {total_money}  {latte_require['cost']}  {total_money >= latte_require['cost']}")
                if total_money >= latte_require["cost"]:
                    print("Your Coffee")
                    resources["water"] = resources["water"] - latte_require["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - latte_require["ingredients"]["coffee"]
                    resources["milk"] = resources["milk"] - latte_require["ingredients"]["milk"]
                    resources["Money"] = resources["Money"] + latte_require["cost"]
                    if total_money > latte_require["cost"]:
                        print(f"Please take your change: {round(total_money - latte_require['cost'], 2) }")
                else:
                    print("Sorry Don't have enough Money! Please Take your refunds")

        case 'cappuccino':
            cappuccino_require = MENU['cappuccino']
            if cappuccino_require["ingredients"]["water"] > resources["water"] :
                print("Not Enough Water")
            elif cappuccino_require["ingredients"]["coffee"] > resources["coffee"]:
                print("Not Enough Coffee")
            elif cappuccino_require["ingredients"]["milk"] > resources["milk"]:
                print("Not Enough coffee")
            else:
                total_money = count_money()
                if total_money >= cappuccino_require["cost"]:
                    print("Your Coffee")
                    resources["water"] = resources["water"] - cappuccino_require["ingredients"]["water"]
                    resources["coffee"] = resources["coffee"] - cappuccino_require["ingredients"]["coffee"]
                    resources["milk"] = resources["milk"] - cappuccino_require["ingredients"]["milk"]
                    resources["Money"] = resources["Money"] + cappuccino_require["cost"]
                    if total_money > cappuccino_require["cost"]:
                        print(f"Please take your change: {round(total_money - cappuccino_require['cost'], 2) }")
                else:
                    print("Sorry Don't have enough Money! Please Take your refunds")
    print(f"Remaining Resources: {resources}")
    return True


while not is_off:
    if type_of_coffee == 'off':
        print("Exit")
        is_off = True
    elif type_of_coffee == 'reports':
        print(f"Reports here: {resources}")
        type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    else:
        is_enough_resource(type_of_coffee)
        type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()



