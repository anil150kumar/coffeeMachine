# show prompt message for entering type of coffee
type_of_coffee = ''

is_off = False

while not is_off:
    if type_of_coffee == 'off':
        print("Exit")
        is_off = True
    else:
        type_of_coffee =  input("What would you like? (espresso/latte/cappuccino): ").lower()
        print(f"{type_of_coffee} ready for serve!");


