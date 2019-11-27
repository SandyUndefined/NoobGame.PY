import random
def main():
    print("Guess a number between 1 to 100")
    rndnumber = random.randint(1,100)
    flag = False
    check = False
    while not flag:
        guess = int(input("Your Guess: "))
        if guess == rndnumber:
            print( "Thats it!")
            ans = input("Do you want to play more?? (YES or No): ")
            if ans == "YES" or ans == "yes":
                flag = False
            else:
                flag = True
        elif guess > rndnumber:
            print( "Guess Lower")
        else:
            print( "Guess Higher")





if __name__ == "__main__":
    main()

