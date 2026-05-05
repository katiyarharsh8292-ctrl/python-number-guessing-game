#hello mene ek number guessing game bnaya
import random
number=random.randint(1,100)
attempt=0
print("welcome to number guessing game!")
print("mene 1 se 100 ke beech number choose kiya hai.")
while True:
    guess=int(input("apna number guess kro:"))
    if guess<number:
        print("too low! thoda bada number try kro.")
    elif guess>number:
        print("too high! thoda chhota number try kro.")
    else:
        print("correct answer!")
        print("total attempt",attempt)
        break