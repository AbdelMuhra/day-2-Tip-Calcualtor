print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15? "))
people = int(input("how many people are going to split the bill? "))
Total_per_Person =total/people +total*(tip/100)/people
final_amount=round(Total_per_Person,2)
print(f"Each person should pay: ${final_amount}")


