import random
user_choice="YES"
positive_choices=['Y', 'YES', 'y', 'yes', 'ok']
while(user_choice in positive_choices):
    my_rand=random.randint(1,100)
    user_option=int(input("Please enter a number:\n"))
    chances=9
    while(user_option!=my_rand and chances>0):
        if(my_rand>user_option):
            print("Too low!\n")
            chances-=1
            user_option=int(input("Please enter a number:\n"))
            continue
        if(my_rand<user_option):
            print("Too high!\n")
            chances-=1
            user_option=int(input("Please enter a number:\n"))
            continue
    if(chances==0):
        user_choice=input("You lost. Want to play again?\n")
    else:
        print("You guessed it right!\n")
        break
    
        
                

