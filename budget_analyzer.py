# smart budget and spending analyzer

expenses = {}
running = True
limits = {
  "food": 300,
  "transport": 150,
  "entertainment": 200
}


print ("Welcome to your personal budget analyzer!")

while running: 
  print ("\nChoose an option:")
  print ("1. add an expense")
  print("2. view spending summary")
  print("3. exit")
    
  choice = input("enter your choice (1-3): ")
  if choice == "1"
    catergory = input("enter expense catergory (food, transport, rent, etc.): ")

    try:
      amount = float(input("enter amount spent: "))
    except ValueError:
      print("invalid amount. please enter a valid number.")

    if category in expenses:
      expenses[catergory].append(amount)
    else:
      expenses[catergory] = [amount]

    print(f"added ${amount:.2f} to {catergory}")

elif choice == "2":
    print("\n--- spending summary ---")

    total spent = 0

# first pass: calculate total spending
for amounts in expenses.values():
  total_spent += sum(amounts)

if total_spent == 0:
  print("no expenses recorded yet.")
  continue

# second pass: calculate catergory totals and percentages
for catergory, amounts in expenses.items():
  catergory_total = sum(amounts)
  percentage = (catergory_total / total_spent) * 100

  print(f"{catergory}: ${catergory_total:.2f} ({percentage:.1f}%)")

    # budget limit check
    if catergory in limits and catergory_total > limits[catergory]:
      print(f" warning: {catergory} spending exceeded the set limit!")

  print(f"\nTotal spent: ${total_spent:.2f}")

  if total_spent > 1000:
    print("overall spending is higher than expected.")
    

    for catergory, amounts in expenses.items():
      catergory_total = sum(amounts)
      total_spent += categrory_total
      print(f"{catergory}: ${catergory_total:.2f}")
    
      if catergory in limits and catergory_total  > limits[catergory]:
        print(f" {catergory} spending exceeded limit !")


    
    print(f"\nTotal Spent: ${total_spent:.2f}")

  if total_spent > 1000:
      print("warning: high spending detected!")

elif choice == "3":
  print ("exiting the program. bye.")
  running = False

else:
  print("invalid choice. please select 1, 2, or 3.")

        
    
