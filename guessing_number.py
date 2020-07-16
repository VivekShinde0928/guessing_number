"""
Author  : Vivek Shinde
Date    : 07/06/2020
purpose : Practice problem solving
code    : guessing a number which is randomly stored in program.player1 & player2 guess that number.show who wins with
          minimum trials
"""
import random
value_a = int(input("Enter the value of a : "))
while True:
        value_b = int(input("Enter the value of b : "))
        if value_a > value_b:
            print("Please enter value greater than a\n")
            continue
        if value_a < value_b:
            break

random_number = random.randint(value_a, value_b)

print(f"\nPlease guess the number between {value_a} and {value_b}")

p1 = 0
p2 = 0
while True:
    player1 = int(input("\nPlayer1 enter Your guess : "))
    p1 = p1 + 1

    if random_number == player1:
        print(f"\n***Player1 took {p1} trials to guess***")
        break
    elif random_number > player1:
        print("Wrong guess! try greater number again ")
    elif random_number < player1:
        print("Wrong guess! try smaller number again ")

# so that player2 cant copy player1 guess
random_number = random.randrange(value_a, value_b)
while True:
    player2 = int(input("\nPlayer2 enter Your guess : "))
    p2 = p2 + 1

    if random_number == player2:
        print(f"\n***Player2 took {p2} trials to guess***")
        break
    elif random_number > player2:
        print("Wrong guess! try greater number again ")
    elif random_number < player2:
        print("Wrong guess! try smaller number again ")

if p1 < p2:
    print("\n*** Player1 Won!!! ***")
elif p2 < p1:
    print("\n*** Player2 Won!!! ***")
else:
    print("\n*** Tie!!!**** ")



