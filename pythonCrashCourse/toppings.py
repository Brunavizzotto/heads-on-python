available_toppings = ['banana', 'yogo', 'strawberry', 'acai', 'grapes', 'kiwi', 'lemon', 'chocolate', 'wine', 'pizza']

requested_toppings = ['banana' , 'caramelo', 'kiwi', 'grapes', 'orange']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"sorry we are out of {requested_topping}.")


print("finished making your froyogo!")