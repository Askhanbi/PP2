#Fucntion 1     Task 13

import random 

print("Hello! What is your name?")
name = input()

print(f"Well {name}, I'm thinking of a number berween 1 and 20: ")
numrandom = random.randint(1,20)
cnt = 0

def GuessTheNumbers(numbers):
    print("Take a guess.")
    num = int(input(""))
    if num < numrandom:
        print("Your guess is too low.")
        return True
    elif num > numrandom:
         print("Your guess is too high. ")
         return True
    else:
        print("Good job, ", name, "! You guessed my number in ", cnt + 1 ," guesses!")
        return False
    
bool = True
while bool:
    bool = GuessTheNumbers(numrandom)
    cnt += 1