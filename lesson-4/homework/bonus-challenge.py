import random
human_score=0
comp_score=0
choices=["rock","paper","scissors"]
while(human_score<5 and comp_score<5):
    comp_choice=random.choice(choices)
    human_choice=input("Enter your choice:\n")
    while(not(human_choice in choices)):
        human_choice=input("Enter your choice correctly:\n")
    print("Comp chose:",comp_choice,".\n")
    if(human_choice==comp_choice):
        print("Draw. Your score:",human_score,".Comp score:",comp_score,".\n")
        continue
    if(human_choice=="rock" and comp_choice=="scissors" or human_choice=="scissors" and comp_choice=="paper" or human_choice=="paper" and comp_choice=="rock"):
        human_score+=1
        print("You win. Your score:",human_score,".Comp score:",comp_score,".\n")
    else:
        comp_score+=1
        print("Comp wins. Your score:",human_score,".Comp score:",comp_score,".\n")

if(human_score==5):
    print("You defeated the comp.")
else:
    print("You are defeated Your score:",human_score,".Comp score:",comp_score)


