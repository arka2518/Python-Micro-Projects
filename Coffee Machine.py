from Menu import MENU, report

profit = 0
continue_order = True

def take_order():
    global profit
    global continue_order
    while continue_order:
        order = input("What would you like, espresso/latte/cappuccino: ").lower()
        if order == 'report':
            print(f"Water: {report['water']}ml\nMilk: {report['milk']}ml\nCoffee: {report['coffee']}g")
        elif order == 'off':
            continue_order = False
        elif order in MENU:
            cost = MENU[order]['cost']
            print(f"Great choice\nHere's your bill: ₹{cost}")
            
            pay = float(input("Please insert the amount: ₹"))
            change = pay - cost
            if change < 0:
                print(f"Sorry, you need ₹{abs(change)} more")
            else:
                print(f"Here is ₹{change} in change")
                profit += cost
                print(f"Profit: {profit}")
                if is_resource_sufficient(order):
                    print(f"Here is your {order}, Enjoy")
                else:
                    print(f"Sorry, not enough resources.\nWe return your ₹{pay}")
                    profit -= cost

def is_resource_sufficient(order):
    ingredients = MENU[order]['ingredients']
    for ingredient, amount in ingredients.items():
        if report[ingredient] < amount:
            return False
    for ingredient, amount in ingredients.items():
        report[ingredient] -= amount
    return True

take_order()