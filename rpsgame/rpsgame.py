import random


computer_wins=0
player_wins=0
 
def users_option():
  user_choice=input("Choose Rock,Paper or Scissors:")
  if user_choice in ["Rock", "rock", "r", "R"]:
    user_choice="r"
  elif user_choice in ["Paper", "paper", "p", "P"]:
    user_choice="p"
  elif user_choice in ["Scissors", "scissors", "s", "S"]:
    user_choice="s"
  else:
    print("Out of choice.")
    users_option()
  return user_choice

def Computer_option():
  comp_choice = random.randint(1,3)
  if comp_choice == 1:
    comp_choice="r"
  elif comp_choice == 2:
    comp_choice="p"
  else:
    comp_choice="s"
  return comp_choice

while True:
    
    user_choice=users_option()
    comp_choice=Computer_option()
    

    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. the computer chose rock.you tied.")

        elif comp_choice == "p":
            print("You chose rock. the computer chose paper.you lose.")
            computer_wins +=1
        elif comp_choice == "s":
            print("You chose rock. the computer chose scissors.you win.")
            player_wins +=1

    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. the computer chose rock.you win.")
            player_wins +=1
        elif comp_choice == "p":
            print("You chose paper. the computer chose paper.you tied.")
            
        elif comp_choice == "s":
            print("You chose paper. the computer chose scissors.you lose.")
            computer_wins +=1  

    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. the computer chose rock.you lose.")
            computer_wins +=1
        elif comp_choice == "p":
            print("You chose scissors. the computer chose paper.you win.")
            player_wins +=1
        elif comp_choice == "s":
            print("You chose scissors. the computer chose scissors.you tied.")

    print("Players wins:" + str(player_wins))
    print("computer wins:" + str(computer_wins))

    user_choice = input("do you want play again? (y/n)")
    if user_choice in ["Y","y","Yes","yes"]:
        pass
    elif user_choice in ["N","n","No","no"]:
        break
    else:
        break
        
   
    


