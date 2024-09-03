#Input we need from user
    #Total rent
    #Total food
    #Electricity per units spend
    #Charge per unit
    #Person living in the room
    
rent = int(input("Enter your hostel/flat rent :- "))
food = int(input("Enter the amount of food spend :- "))
electricity_spend = int(input("Enter the total electricity spend in your room :- "))
charge_per_unit = int(input("Enter the charge(amount)per unit :- "))
persons =int(input("Enter the number of persons living in the room :-"))

#calculate total electricity bill
total_e_bill = electricity_spend * charge_per_unit
print(f"\n Total Electricity bill :- {total_e_bill}")

#claculate total room expenses including rent per person
actual_bill = (rent + food + total_e_bill)/persons
print("\n________________Your bill is ready_______________________")
print(f"\nPer person bill :- {actual_bill}")

#total expenses
total = rent + food + total_e_bill
print(f"Total rent expenses :- {total}")


