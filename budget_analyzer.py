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
  if choice == "1":
    category = input("enter expense category (food, transport, rent, etc.): ")

    try:
      amount = float(input("enter amount spent: "))
    except ValueError:
      print("invalid amount. please enter a valid number.")
      continue

    if category in expenses:
      expenses[category].append(amount)
    else:
      expenses[category] = [amount]

    print(f"added ${amount:.2f} to {category}")

  elif choice == "2":
    print("\n--- spending summary ---")

    total_spent = 0

    for amounts in expenses.values():
      total_spent += sum(amounts)

    if total_spent == 0:
      print("no expenses recorded yet.")
      continue

    for category, amounts in expenses.items():
      category_total = sum(amounts)
      percentage = (category_total / total_spent) * 100

      print(f"{category}: ${category_total:.2f} ({percentage:.1f}%)")

      if category in limits and category_total > limits[category]:
        print(f" warning: {category} spending exceeded the set limit!")

    print(f"\nTotal spent: ${total_spent:.2f}")

    if total_spent > 1000:
      print("overall spending is higher than expected.")

  elif choice == "3":
    print ("exiting the program. bye.")
    running = False

  else:
    print("invalid choice. please select 1, 2, or 3.")
    
