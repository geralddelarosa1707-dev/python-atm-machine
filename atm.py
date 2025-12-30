print("Welcome to Python ATM Machine")

FEATURES = {
  1: "Check Balance",
  2: "Deposit",
  3: "Withdraw",
  4: "Exit"
}

pin = 1234

attempts = 3

balance = 10000

authenticated = False

def is_pin_correct(entered_pin, correct_pin):
  return entered_pin == correct_pin

def show_menu():
  print("\n-----Options:-----")
  for i, feature_name in FEATURES.items():
    print(f"{i}. {feature_name}")

def is_valid_deposit(amount):
  return amount > 0

def can_withdraw(amount, balance):
  if amount <= 0:
    print("\nAmount must be greater than 0.")
    return False
  if amount > balance:
    print("\nInsufficient balance.")
    return False
  return True

while attempts > 0:
  try:
    try_pin = int(input("\nPlease enter your PIN: "))
  except ValueError:
    print("\nPlease enter a valid PIN.")
    continue

  valid_pin = is_pin_correct(try_pin, pin)
  
  if valid_pin:
    authenticated = True
    print("\nPIN accepted. You can now proceed with your transactions.")
    break
  else:
    attempts -= 1
    print(f"\nIncorrect PIN. You have {attempts} attempt/s left.")
    
    if attempts == 0:
      print("\nPlease try again later.")
      break

def run_atm(balance):
  while True:
    show_menu()
    
    try:
      choose_feat = int(input("\nPlease select a feature (1-4): "))
    except ValueError:
      print("\nPlease enter a valid number.")
      continue
    
    if choose_feat == 1:
      print(f"\nYour current balance is ₱{balance:.2f}")
      
    elif choose_feat == 2:
      try:
        deposit = float(input("\nEnter the amount you want to deposit: "))
      except ValueError:
        print("\nPlease enter a valid amount.")
        continue
  
      valid_deposit = is_valid_deposit(deposit)
      
      if valid_deposit:
        balance += deposit
        print(f"\nDeposit successful. Your new balance is ₱{balance:.2f}")
      else:
        print("\nAmount must be greater than 0.")
        continue
        
    elif choose_feat == 3:
      print(f"\nYour current balance is ₱{balance:.2f}")
  
      try:
        withdraw = float(input("\nEnter the amount you want to withdraw: "))
      except ValueError:
        print("\nPlease enter a valid amount.")
        continue
      
      valid_withdraw = can_withdraw(withdraw, balance)
  
      if valid_withdraw:
        balance -= withdraw
        print(f"\nWithdrawal successful. Your new balance is ₱{balance:.2f}")
      else:
        continue
      
    elif choose_feat == 4:
      print("\nThank you for using Python ATM Machine!")
      break
      
    else:
      print("\nPlease select a valid option.")

if authenticated:
  run_atm(balance)