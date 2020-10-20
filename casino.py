#Facundo Yan 24/8/20
#adding comment 2
import random


deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
roul = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,27,10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]
def coinflip(what, bet):
  print("You are now playing a coinflip!")
  result = what.lower()[0]
  
  num = random.randint(0,1)
  if num == 0:
    end = 'Heads'
  else:
    end = 'Tails'
  
  print('It\'s ' + end + '!')

  if result in ['h', 't']:
    if result == end.lower()[0]:
      print('You won!')
      return bet
    else:
      print("You lost...")
      return -bet
  else:
    print("You didn't choose neither heads nor tails!")
    return 0


def chohan(what, bet):
  print("You are now playing Cho-Han!")
  choice = what.lower()[0]
  if choice in ['o', 'e']:
    if choice == 'o':
      final = 1
    else:
      final = 0
  else:
    print("You didn't choose neither odd nor even!")
    return 0

  gen = random.randint(1,6) + random.randint(1, 6)
  print('The number is {}!'.format(gen))
  result = gen % 2

  if final == result:
    print("You won!")
    return bet
  else:
    print("You lost...")
    return -bet
    
    
def higher_card(bet):
  print("You are now playing Higher Card!")
  temp = deck
  first = random.randint(0,51)
  player1 = temp.pop(first)
  print("Your card is {}!".format(player1))
  second = random.randint(0,50)
  player2 = temp.pop(second)
  print("Your opponent's card is {}!".format(player2))
  if player1 > player2:
    print('You won!')
    return bet
  elif player2 > player1:
    print("You lost...")
    return -bet
  else:
    print("It's a tie!")
    return 0


def roulette(what, bet):
  print("You are now playing Roulette!")
  gen = roul[random.randint(0,36)]
  print("The number is {}!".format(gen))
  if type(what) == str:
    choice = what.lower()[0]
    if choice in ['o', 'e']:
      if choice == 'o':
        final = 1
      else:
        final = 0
    else:
      print("You didn't choose neither odd nor even!")
      return 0

    result = gen % 2

    if gen == 0 or gen == 00:
      print("You lost...")
      return -bet
    else:
      if final == result:
        print("You win!")
        return bet
      else:
        print("You lost...")
        return -bet

  elif type(what) == int:
    if what not in roul:
      print("You did not choose a number on the roulette!")
      return 0
    else:
      if gen == what:
        print('You won!')
        return 35 * bet
      else:
        print('You lost...')
        return -bet

def check(money):
  print("You currently have ${}".format(money))
    


def play():
  money = 100
  print('Welcome to the Casino!')
  choice = None
  while choice != 7:
    print("1. Coinflip")
    print("2. Cho-Han")
    print("3. Higher Card")
    print("4. Roulette")
    print("5. Check money")
    print("6. Add money")
    print("7. Exit Casino")
    choice = int(input("What do you want to do? "))
    if choice == 1:
        what = input("Please enter 'Heads' or 'Tails': ")
        bet = int(input("Please enter the bet: "))
        money += coinflip(what, bet)
        check(money)
    elif choice == 2:
        what = input("Please enter 'Odd' or 'Even': ")
        bet = int(input("Please enter the bet: "))
        money += chohan(what, bet)
        check(money)
    elif choice == 3:
        bet = int(input("Please enter the bet: "))
        money += higher_card(bet)
        check(money)
    elif choice == 4:
        print("1. Odd or Even")
        print("2. Number Guessing")
        game = None
        while game not in [1,2]:
            game = int(input("Please enter the type of bet you want to make: "))
            if game == 1:
                what = input("Please enter 'Odd' or 'Even': ")
                bet = int(input("Please enter the bet: "))
                money += roulette(what, bet)
                check(money)
            elif game == 2:
                what = input("Please enter the number you are betting for: ")
                bet = int(input("Please enter the bet: "))
                money += chohan(what, bet)
                check(money)
            else:
                print("You did't enter neither 1 nor 2!")
    elif choice == 5:
        check(money)
    elif choice == 6:
        amount = int(input("Please enter the amount you want to add: "))
        money += amount
    elif choice not in range(1,8):
        print("You haven't chosen a valid option!")
    
    print()



    
    




play()
