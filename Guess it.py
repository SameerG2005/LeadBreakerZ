import random
count=0
for i in range(1,7):
    generate= random.randint(1,6)
    guess=int(input("Guess The No.:"))
    if guess == generate:
        print("Nice Guess")
        print()
        count=count+1
    elif guess>6:
        print("Type less than 6")
    elif guess<0:
        print("Type more than 0")
    else:
        print("Wrong guess,No.is= ",generate)
        print()
    print("Your Score: ",count)
    
if count>3:
    print("WEll PLAYED... YOU W!N")
if count<3:
    print("Better LUCK NEXT TIME... YOU LOOSE")
