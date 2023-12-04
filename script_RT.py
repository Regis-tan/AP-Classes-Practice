from classes_RT import food_RT

while True:
    food_amount = int(input("Enter how many items you will order today: "))
    if food_amount <= 0:
        print("You need to order atleast 1 item.")
        pass
    else:
        break

food_list = []

for i in range(food_amount):
    print(f"Item #{i+1}-")
    food_order = str(input("Enter food: "))
    pounds_order = float(input("Enter amount of pounds: "))
    
    my_order = food_RT(food_order,pounds_order)
    food_list.append(my_order)

total_price = 0

print("Here is a summary of your purchases: ")
print("-"*20)
for i in food_list:
    print(f"Item: {i.get_name_RT()}")
    print(f"Amount ordered: {i.get_amount_RT()} pounds")
    print(f"Price per pound: ${i.get_ppp_RT()}")
    print(f"Price of order: ${i.calculate_price_RT()}")
    print()
    total_price += i.calculate_price_RT()

print(f"Total cost: ${total_price}")
