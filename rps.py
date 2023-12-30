#rock-paper-scissors game with continue function
import random
print('Rock-Paper-Scissors!')
playerWins = 0
computerWins = 0

def rps():
  global playerWins
  global computerWins
  while True:
    playerMove = input('Select move (r, p, or s): ')
    if playerMove=='r' or playerMove=='p' or playerMove=='s':
      break
    else:
      print("Invalid player input.  Player input must be 'r', 'p', or 's'")
  
  computerInput = random.randint(1,3)

  if computerInput==1:
    computerMove='r'
  elif computerInput==2:
    computerMove='p'
  elif computerInput==3:
    computerMove='s'
  else:
    print('computerInput outside expeted range')
    return
  
  print('Player chose '+playerMove+'.  Computer chose '+computerMove+'.')
  if playerMove=='r':
    if computerMove=='r':
      print('Tie.')
    elif computerMove=='p':
      print('You lose.')
      computerWins+=1
    elif computerMove=='s':
      print('You win!')
      playerWins+=1
  elif playerMove=='p':
    if computerMove=='r':
      print('You win!')
      playerWins+=1
    elif computerMove=='p':
      print('Tie.')
    elif computerMove=='s':
      print('You lose.')
      computerWins+=1
  elif playerMove=='s':
    if computerMove=='r':
      print('You lose.')
      computerWins+=1
    elif computerMove=='p':
      print('You win!')
      playerWins+=1
    elif computerMove=='s':
      print('Tie.')

while True:
  rps()
  print('Player: '+str(playerWins)+'  Computer: '+str(computerWins))
  print('Play Again? (y/n)')
  cont = input()
  if cont == 'n':
    break