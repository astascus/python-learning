import random

MAX_DENOM = 100

class Card ():
  def __init__(self,suit,number):
    self.suit = suit
    self.number = number
    

cardNumbers = [2,3,4,5,6,7,8,9,'T','J','Q','K','A']
cardSuits = ['C','D','S','H']

#deck = [Card(suit, number) for suit in cardSuits for num in cardNumbers]

def createDeck(suits,numbers):
  deck=[]
  for suit in suits:
    for num in numbers:
      c = Card(suit,num)
      deck.append(c)
  return deck

def shuffleDeck(deck):
  if deck:
    random.shuffle(deck)
  
  return deck

def displayHand(deck):
  for i in range(5):
    print(deck[i].suit + str(deck[i].number), end="  ")
  print()
  for i in range(5):
    print(i, end="   ")
  print()
  

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def setBalance():
  while True:
    balance = input("What is your starting balance? $")
    if is_float(balance):
      balance = float(balance)
      if balance > 0:
        break
      else:
        print("Enter a value greater than 0")
    else:
      print("Enter a number")
  return balance

def setDenomination():
  while True:
    denom = input("What denomination? ")
    if is_float(denom):
      denom = float(denom)
      if 0< denom <= MAX_DENOM:
        break
      else:
        print("Enter a valid denomination")
    else:
      print("Enter a number")

  return denom

def setCoins():
  while True:
    coins = input("How many coins to bet (1-5)?  ")
    if coins.isdigit():
      coins = int(coins)
      if 0<= coins <= 5:
        break
      else:
        print("Enter a valid number of coins")
    else:
      print("Enter a number between 1 and 5")

  return coins

def replaceCards(deck, choices):
  if choices[0] != '':
    for i in range(len(choices)):
      temp = deck[int(choices[i])]
      deck[int(choices[i])] = deck[5+i]
      deck[5+i] = temp

  return deck

def checkWin(deck):
  winnings = 0
  def is_royal(card):
    if card.number == 10 or card.number == 'J' or card.number == 'Q' or card.number == 'K' or card.number == 'A':
      return True
    else:
      return False

  def is_flush(deck):
    if deck[0].suit == deck[1].suit and deck[0].suit == deck[2].suit and deck[0].suit == deck[3].suit and deck[0].suit == deck[4].suit:
      return True
    else:
      return False

  def convertFace(deck):
    for i in range(5):
      if deck[i].number == 'T':
        deck[i].number = 10
      elif deck[i].number == 'J':
        deck[i].number = 11
      elif deck[i].number == 'Q':
        deck[i].number = 12
      elif deck[i].number == 'K':
        deck[i].number = 13
      elif deck[i].number == 'A':
        deck[i].number = 14
    return deck
  
  def convertToFace(deck):
    for i in range(5):
      if deck[i].number == 10:
        deck[i].number = 'T'
      elif deck[i].number == 11:
        deck[i].number = 'J'
      elif deck[i].number == 12:
        deck[i].number = 'Q'
      elif deck[i].number == 13:
        deck[i].number = 'K'
      elif deck[i].number == 14:
        deck[i].number = 'A'
    return deck
    
  def is_straight(deck):
    a = []
    deck = convertFace(deck)
    for i in range(5):
      a.append(deck[i].number)
    a.sort()
    for i in range(4):
      if a[i+1]-a[i] != 1:
        break
    else:
      deck=convertToFace(deck)
      return True
    deck=convertToFace(deck)
    return False
  
  def is4oak(deck):
    matchCount=0
    for i in range(4):
      for j in range(i+1,5):
        if deck[i].number == deck[j].number:
          matchCount+=1
    if matchCount==3:
      return True
    else:
      return False

  def is3oak(deck):
    matchCount=0
    breakFlag = False
    toakNum = 0
    for i in range(4):
      for j in range(i+1,5):
        if (deck[i].number == deck[j].number) and deck[i].number == toakNum:
          matchCount=2
          breakFlag=True
          break
        elif deck[i].number == deck[j].number:
          toakNum = deck[i].number
          matchCount=1
        if breakFlag:
          break

    if matchCount==2:
      return True
    else:
      return False
    
  def is_pair(deck):
    matchCount=0
    for i in range(4):
      for j in range(i+1,5):
        if deck[i].number == deck[j].number:
          matchCount+=1
    if matchCount==1:
      return True
    else:
      return False
    
  def is2pair(deck):
    pairCount=0
    breakFlag = False
    for i in range(4):
      for j in range(i+1,5):
        if deck[i].number == deck[j].number:
          pairNum = deck[i].number
          pairCount+=1
          breakFlag = True
          break
      if breakFlag:
        break

    for i in range(4):
      for j in range(i+1,5):
        if (deck[i].number == deck[j].number) and deck[i].number != pairNum:
          pairCount+=1 
    if pairCount==2:
      return True
    else:
      return False
    
  def is_jack_pair(deck):
    matchCount=0
    convertFace(deck)
    for i in range(4):
      for j in range(i+1,5):
        if (deck[i].number == deck[j].number) and deck[i].number > 10:
          matchCount+=1
    if matchCount==1:
      deck = convertToFace(deck)
      return True
    else:
      deck = convertToFace(deck)
      return False

  if is_flush(deck) and is_royal(deck[0]) and is_royal(deck[1]) and is_royal(deck[2]) and is_royal(deck[3]) and is_royal(deck[4]): #royal flush
    print("Royal Flush")
    winnings = 250
  elif is_flush(deck) and is_straight(deck): #straight flush
    print("Straight Flush")
    winnings = 50 
  elif is4oak(deck): #4 of a kind
    print("Four of a Kind")
    winnings = 25
  elif is_pair(deck) and is3oak(deck):#full house
    print("Full House")
    winnings = 9
  elif is_flush(deck):#flush
    print("Flush")
    winnings = 6
  elif is_straight(deck):#straight
    print("Straight")
    winnings = 4  
  elif is3oak(deck): #3 of a kind
    print("Three of a Kind")
    winnings = 3
  elif is2pair(deck):#two pair
    print("Two Pair")
    winnings = 2
  elif is_jack_pair(deck):#jacks or better
    print("Pair Jacks or Better")
    winnings = 1
  else:
    print("You Lose")
  return winnings

def setupGame():
  denom = setDenomination()
  coins = setCoins()
  return denom, coins

def game(deck, denom, coins):
  totalBet = coins*denom
  print(f'Betting {coins}x${denom} for total bet ${totalBet}')
  deck = shuffleDeck(deck)
  displayHand(deck)
  while True:
    choices = input("Which cards to replace? ").split(" ")
    if len(choices)>5:
      print("Too many cards chosen")
    else:
      break
  deck = replaceCards(deck,choices)
  displayHand(deck)
  win = checkWin(deck)
  totalWin = win*coins*denom
  if win == 250 and coins == 5:
    totalWin = 4000*denom
  print(f'You win ${totalWin}')
  return totalWin - totalBet

def main():
  deck = createDeck(cardSuits,cardNumbers)
  breakFlag = False
  #print(deck[12].suit + str(deck[12].number))
  balance = setBalance()
  print(f"Starting balance: ${balance}")
  while True:
    denom, coins = setupGame()
    while True:
      balance += game(deck, denom, coins)
      print(f'Balance: ${balance}')
      print("Play again?\n  'n' = no\n  'c'= change bet\n  Any other key plays again")
      choice = input("Play again?")
      if choice == 'n':
        breakFlag=True
        break
      elif choice =='c':
        break
    if breakFlag:
      break
  print(f'you walk away with ${balance}')

    
main()
