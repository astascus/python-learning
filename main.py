import random

#constants for machine
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#size of the play area
ROWS = 3
COLS = 3

#reels build
symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
      
    else: #this is a for-else statement.  else executes if for does not break
      winnings += values[symbol]*bet
      winning_lines.append(line +1)

  return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
  #this section is reading in all the symbols we defined in the symbol_count dictionary and building all_symbols array
  all_symbols = []
  for symbol, symbol_count in symbols.items(): #look into this syntax, it's referring to the symbol_count dictionary where symbol is the first value of a pair and symbol_count is the second value of a pair.  This works because the dictonary defined above is what we'll pass into the function as an argument
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  #this section builds the three columns we want in our slot machine
  columns = []
  for _ in range(cols):  #_ is an "anonymous varialbe".  same thing as i but you don't have to declare another variable
    column = []
    current_symbols = all_symbols[:] #the colon creates a copy of the array, without the [:] this would create an additional reference to the same data
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)

    columns.append(column)

  #print(columns)
  return columns

def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):  #video says enumerate allows you to get the index into i and also get a value into column
      if i != len(columns)-1:
        print(column[row], end=" | ") #end lets you contine printing on the same line.  by default, it's set to \n
      else:
        print(column[row], end = "")
    print() #this blank print is acting like a return

def deposit():
  while True:
    amount = input("What would you like to deposit?  $")
    if amount.isdigit():
      amount = int(amount)
      if amount >0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number")
  return amount

def get_number_of_lines():
  while True:
    lines = input("Enter the number of lines to bet on (1-" +str(MAX_LINES)+")? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Enter a valid number of lines.")
    else:
      print("Please enter a number")
  return lines

def get_bet():
  while True:
    amount = input("What would you like to bet on each line?  $")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
    else:
      print("Please enter a number")
  return amount

def main():
  balance = deposit()
  while True:
    lines = get_number_of_lines()
    while True:
      bet = get_bet()
      totalBet = lines * bet
      if totalBet > balance:
        print("You do not have enough to bet that amount")
        print(f"Your current balance is ${balance}")
      else:
        break
    print(f"You are betting ${bet} on {lines} lines.  Total bet is ${totalBet}.")
    balance -= totalBet
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    #slots = [['A','A','A'],['A','B','A'],['A','C','A']]
    print_slot_machine(slots)
    winnings, winning_lines= check_winnings(slots,lines,bet,symbol_value)
    if winnings > 0:
      if len(winning_lines) > 1:
        print(f'Lines ', end="")
        for i in range(len(winning_lines)):
          if i == len(winning_lines)-1:
            print(f'and {winning_lines[i]}', end="")
          else:
            print(winning_lines[i], end=", ")
        print(' are winners!')
      else:
        print(f'Line {winning_lines[0]} is a winner!')
      print(f'You won ${winnings}!')
      balance += winnings
    else:
      print("You lose.")
    print(f'Current balance: ${balance}')
    print("Would you like to play again? (y/n)")
    if input() == 'n':
      break


main()
  