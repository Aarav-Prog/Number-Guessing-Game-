import random
secret_number = random.randrange(1, 120)
guess_count = 0
guess_limit = 6
print("Welcome to a Number guessing game made by Aarav ")
print("Instructions: ")
print("You will be given 6 chances .")
print( " The computer will take a random num btw 1 to 20 and you have to guess it")

while guess_count < guess_limit:
 guess = int(input('Guess: '))
 guess_count += 1
 if guess == secret_number:
   print("you won")
   break
 else:
  print("Sorry Wrong answer")











