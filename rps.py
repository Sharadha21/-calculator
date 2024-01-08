import random
options=['rock','paper','scissor']

def game():
    select=random.choice(options)

    print(" rock")
    print("paper")
    print("scissor")
    ch=input("Enter your choice\n")
    print('Computer choice is ',select)

    if select==ch:
        print('Game is Tie')
    else:
        if select=='rock' :
            if ch=='paper':
                print('You won')
            elif ch=='scissor':
                print('You loss')
        elif select=='paper':
            if ch=='rock':
                print('You loss')
            else:
                print('You won')
        elif select=='scissor':
            if ch=='rock':
                print('You won')
            elif ch=='paper':
                print('You loss')
game()
while True:
    print('Do you Want to continue : ')
    c=input()
    if c=='y':
        game()
    else:
        break;

                
                
                
    
                
                
            