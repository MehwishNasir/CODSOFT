import random


rock = "r"or "R"
scissors = "s"or "S"
paper = "p"or "P"
def game(user,comp):
    if user == rock and comp == "scissors":
       print("YOU WIN")
    elif user == scissors and comp == "paper":
       print("YOU WIN") 
    elif user == paper and comp == "rock":
       print("YOU WIN") 
    elif user == scissors and comp == "rock":
       print("YOU LOSE") 
    elif user == paper and comp == "scissors":
       print("YOU LOSE")
    elif user == rock and comp == "paper":
       print("YOU LOSE")        
    elif user == rock and comp == "rock" or user == scissors and comp == "scissors" or user == paper and comp == "paper" :
       print("Its's a draw!")
    else: 
       print("Choose Again")  



a = "y"
choice = ["rock" , "paper" , "scissors"]
while a == "y"or a =="Y":
   comp = random.choice(choice)
   user = input("Enter your choice: r/R for rock , s/S for scissors and p/P for paper :")
   print("Computer's choice :",comp)

   if user == rock:
      print("You choose rock")
   elif user == scissors:
      print("You choose scissors") 
   elif user == paper:
      print("You choose paper")  
   else: 
      print("Incorrect choice ! Choose the correct option") 
   game(user,comp)  
   a = input("Want's to try again!(y/n)")  
   if a == "y"or"Y":
      continue
   elif a =="n" or "N":
      print("Thanks for Playing")
      break