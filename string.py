import random
winning_number = random.randint(1,101)
guess = 1
number = int(input("Guess a number between 1 and 100: "))
game_over = False
while not game_over:
    if number == winning_number:
        print(f"YOU WIN!!!!\U0001F609 ,and guessed the number in {guess} times  ")
        game_over = True
    else:
      if number < int(winning_number):
            print("TOO LOW\U0001F607   ")
            guess += 1
            number =int(input("GUESS AGAIN: "))
      else:
            print("TOO HIGH\U0001F608    ")   
            guess += 1
            number = int(input("GUESS AGAIN: "))         