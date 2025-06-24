menu={
    'latte':{
        'needs':{   
            'water':100,
            'milk':75,
            'coffee':20
        },
        'cost':150,
    },
    'cappuccino':{
        'needs':{   
            'water':100,
            'milk':100,
            'coffee':28
        },
        'cost':200,
    },
    'espressso':{
        'needs':{   
            'water':100,
            'milk':50,
            'coffee':35,
        },
        'cost':170,
    },
    
}
profit=0
ingrediants={
    'milk':200,
    'water':500,
    'coffee':100,
}
def check_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>ingrediants[item]:
            print(f'Sorry there is not enough{item}')
            return False
        return True

def process_money():
    print('Please enter the money!')
    total=0
    five_coins=int(input('How many 5rs coins: '))
    ten_coins=int(input('How many 5rs coins: '))
    twenty_coins=int(input('How many 5rs coins: '))
    total=five_coins*5+ten_coins*10+twenty_coins*20
    return total

def is_payment_successful(money_recived,coffee_cost):
    if money_recived>=coffee_cost:
        global profit
        profit=profit+coffee_cost
        change=coffee_cost-money_recived
        print(f'Here is your rs{change} change')
        return True
    else:
        print("Sorry money is not enough..,money refunded")
        return False
    
def make_coffee(coffee_name,coffee_needs):
    for item in coffee_needs:
        ingrediants[item] -= coffee_needs[item]

    print(f'Here is your {coffee_name} ☕....!Enjoy')       

while True:
    choice=input("Would you like to have(cappuccino,latte, espresso): ").lower()
    # if choice == ['cappuccino','latte', 'espresso']:
    #     print('Please enter valid coffee')
    if choice == "off":
        break
    elif choice == 'report':
        print(f"Coffee:{ingrediants['coffee']}g")
        print(f"Milk:{ingrediants['milk']}ml")
        print(f"Water:{ingrediants['water']}ml")
        print(f'Earned money {profit}')
    else:
        coffee_type=menu[choice]
        print(coffee_type)
        if check_resource(coffee_type['needs']):
            payment=process_money()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(choice,coffee_type['needs'])
        
