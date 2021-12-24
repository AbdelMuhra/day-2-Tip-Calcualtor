print("Welcome to the tip calculator!")
total = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10,12 or 15? ")
people = input("how many people are going to split the bill? ")
Total_per_Person =float(total)/int(people) + (float(total)*(float(tip)/100))/int(people)
final_amount=round(Total_per_Person,2)
print(f"Each person should pay: ${final_amount}")


