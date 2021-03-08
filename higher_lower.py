import random
from data_set import data
repeat=True
while repeat:
    score=0
    right=True
    while right:
        acc_1=random.choice(data)
        acc_2=random.choice(data)
        while acc_1==acc_2:
            acc_2=random.choice(data)
        print(f" a. {acc_1['name']}")
        print(f" b. {acc_2['name']}")
        user=input("Which of the celebrity has more Followers on Instagram, Choose 'a' or 'b': ")
        a=acc_1
        b=acc_2

        if acc_1['followers']>acc_2['followers']:
            answer=a
        else:
            answer=b

        if user=="a" and answer==a:
            print("Correct!")
            print(answer['Statement'])
            score+=1
            right=True
        elif user=="b" and answer==b:
            print("Correct!")
            print(answer['Statement'])
            score+=1
            right=True

        else:
            print("Wrong!")
            print("Correct Answer is " + answer['name'])
            print(answer['Statement'])
            right=False
            print(f"Your score was {score}")
    u_repeat=input("Do you want to play again? 'y' for yes 'n' for no: ")
    if u_repeat=="y":
        repeat=True
    else:
        repeat=False


