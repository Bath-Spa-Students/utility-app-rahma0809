#Items available:-Choclates, Chips, Drinks,Biscuits

# Menu of food items available in the vending machine

Chocolates=[{# list of varities of the item
    'itemno':'1',
    'item_name':'Kinder Bueno', 
    'item_price':'4.50'},
    
    {'itemno':'2',
     'item_name':'Kitkat',
     'item_price':'3'},
     
     {'itemno':'3',
       'item_name':'Flakes',
       'item_price':'3.50'},

       {'itemno':'4',
        'item_name':'Galaxy',
        'item_price':'4',},]


Snacks=[{'itemno':'5',
        'item_name':'Finns',
        'item_price':'5'},

        {'itemno':'6',
        'item_name':'Lays',
        'item_price':'5.50'},
        
        {'itemno':'7',
         'item_name':'Doritos',
          'item_price':'7'},
          
          {'itemno':'8',
           'item_name':'Bugles',
           'item_price':'6.50'},
           
           {'itemno':'9',
            'item_name':'Pringles',
            'item_price':'8',},]


Drinks=[{'itemno':'10',
         'item_name':'Pepsi',
         'item_price':'3'},
         
         {'itemno':'11',
          'item_name':'Mango juice',
          'item_price':'2.50'},
          
          {'itemno':'12',
           'item_name':'Cold coffee',
           'item_price':'5.50'},
           
           {'itemno':'13',
            'item_name':'Hot choclate',
            'item_price':'7.50'},

            {'itemno':'14',
             'item_name':'Water',
            'item_price':'2',},]


Biscuits=[{'itemno':'15',
           'item_name':'Digestives',
           'item_price': '6'},

           {'itemno':'16',
            'item_name':'Bourbon',
            'item_price':'7.50'},
             
             {'itemno':'17',
             'item_name':'Choco cookies',
              'item_price':'5.50'},
            
            {'itemno':'18',
            'item_name':'Ginger biscuits',
             'item_price':'4.50'},
            
            {'itemno':'19',
            'item_name':'Custard and cream',
             'item_price':'7',},]

# List to store purchased item
item= []

# Flag to control the vending machine loop
run = True

# printing the Menu
print('''
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀▄▀█ █▄█   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █░▀░█ ░█░   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄*****\n\n''')

print('-------------------------- The Items available at the moment are:--------------------------\n\n')

# Printing the menu items for each catergory
for i in Chocolates:
    print(f"Itemno: {i['itemno']}   ----Item: {i['item_name']}   ----Price: {i['item_price']}")

for i in Snacks:
    print(f"Itemno: {i['itemno']}   ----Item: {i['item_name']}   ----Price: {i['item_price']}")

for i in Drinks:
    print(f"Itemno: {i['itemno']}   ----Item: {i['item_name']}   ----Price:{i['item_price']}")

for i in Biscuits:
    print(f"Itemno:{i['itemno']}    ----Item: {i['item_name']}   ----Price: {i['item_price']}")
print('--------------------------------------------------------------------------------------------\n\n')

# Function to stimulate the vending machine process
def machine(Chocolates, Snacks, Drinks, Biscuits, run, item):

    while run:


        print("Enter the item number to purchase, or 'q' to exit.")

        user_input = input('Your choice: ')

       

        if user_input.lower() == 'q':

            run = False

        else:

            try:

                buy_item = int(user_input)

                # check the item category and add it to the 'item' list
                if 1 <= buy_item <= len(Chocolates):

                    item.append(Chocolates[buy_item - 1])

                elif len(Chocolates) < buy_item <= len(Chocolates) + len(Snacks):

                    item.append(Snacks[buy_item - len(Chocolates) - 1])

                elif len(Chocolates) + len(Snacks) < buy_item <= len(Chocolates) + len(Snacks) + len(Drinks):

                    item.append(Drinks[buy_item - len(Chocolates) - len(Snacks) - 1])

                elif len(Chocolates) + len(Snacks) + len(Drinks) < buy_item <= len(Chocolates) + len(Snacks) + len(Drinks) + len(Biscuits):

                    item.append(Biscuits[buy_item - len(Chocolates) - len(Snacks) - len(Drinks) - 1])

                else:

                    print('Invalid item number!')

            except ValueError:

                print('Invalid input! Please enter a valid item number or "q" to exit.')

    return item


# Function to calculate the total price of purchased items 
def sum_item(item):

    return sum(float(product['item_price']) for product in item)

 
# Function to create a receipt for purchased items
def create_receipt(item):

    receipt = "\n\n************ Receipt ************\n"

    for i in item:

        receipt += f"\nItem: {i['item_name']}\tPrice: {i['item_price']}"

    receipt += f"\n\nTotal Price: {sum_item(item)}"

    return receipt 

# Function to get the amount of money from the user and calculate the total change
def get_money(amount):
    money = float(input('Enter the amount of money you have: '))
    while money < amount:
        print("You don't have enough money")
        money = float(input('Ente the amount of money you have'))
    change = money - amount
    return change

# Simulate the vending machine process
Chocolates = [{"item_name": "Kinder Bueno", "item_price": 4.50},
              {"item_name": "Kitkat",'item_price':3},
              {'item_name':'Flakes','item_price':3.50},
              {'item_name':'Galaxy','item_price':4},]

Snacks = [{"item_name": 'Finns','item_price':5},
          {"item_name":'Lays','item_price':5.50},
          {'item_name':'Doritos','item_price':7},
          {'item_name':'Bugles','item_price':6.50},
          {'item_name':'Pringles','item_price':8},]

Drinks = [{"item_name":'Pepsi','item_price':'3' },
          {"item_name":'Mango juice','item_price':2.50 },
          {'item_name':'Cold coffee','item_price':5.50},
          {'item_name':'Hot choclate','item_price':7.50},
          {'item_name':'Water','item_price':'2'},]

Biscuits = [{"item_name": "Digestive", "item_price": 6},
            {"item_name":'Bourbon','item_price':7.50 },
            {'item_name':'Choco cookies','item_price':5.50},
            {'item_name':'Ginger biscuits','item_price':4.50},
            {'item_name':'Custard and cream','item_price':7},]

run = True

item = []

# Call the machine function to simulate the vending machine process
item= machine(Chocolates, Snacks, Drinks, Biscuits, run, item)

# Get the change from the user
change = get_money(sum_item(item))

# Display the receipt and change
print(create_receipt(item))
print(f"\nYour change is: {change}\n")

# Display a Thank you message.
print('*********************************************************************************************\n')
print('Thank you for purchasing. Have a good day !!\n')
print('*********************************************************************************************\n')
