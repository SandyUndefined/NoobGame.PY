import random
def main():
    print("Guess a number between 1 to 100")
    rndnumber = random.randint(1,100)
    flag = False
    c=0
    while not flag:
        guess = int(input("Your Guess: "))
        if guess == rndnumber:
            print("Your guess is Correct")
            print(f'You took ',c+1,f'Chances')
            ans = input("Do you want to play more?? (YES or No): ")
            if ans == "YES" or ans == "yes":
                flag = False
            else:
                flag = True
        elif guess > rndnumber:
            print( "Guess Lower")
            c+=1
        else:
            print( "Guess Higher")
            c+=1





if __name__ == "__main__":
    main()

