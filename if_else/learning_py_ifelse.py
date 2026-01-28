request_toppings = ['mushrooms', 'onions', 'pineapple']
avaible_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                    'pineapple', 'extra cheese']

if('mushrooms' in request_toppings):
    print("is in request_toppings")

for request_topping in request_toppings:
    if(request_topping in avaible_toppings):
        print(f"adding {request_topping}")
    else:
        print(f"sorry, we dont have {request_topping}")