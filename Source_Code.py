import random
lis=['Rock','Paper','Scissors']
rps_dic={"Rock":'💎',"Paper":'📝',"Scissors":'✂️'}
while True:
  print("""
1 Play Game ✅
5 Exit Game ❌
  """)
  player_choice=int(input("Enter 1 or 5 -> "))
  if player_choice==1:
    print("""
---🏆 The winning rules are 🏆---

-> Rock vs paper-> paper wins
-> Rock vs scissor-> Rock wins
-> paper vs scissor-> scissor wins""")
    computer=0
    user=0
    import math
    user_input=math.inf
    while  user_input!=5:
      print("""
1 "Rock 💎"
2 "Paper 📝"
3 "Scissors ✂️"
      """)
      user_input=int(input("Enter 1 or 2 or 3 -> "))
      print()
      if user_input==1:
        user_input="Rock"
      elif user_input==2:
        user_input="Paper"
      elif user_input==3:
        user_input="Scissors"
      else:
        print("Your choice is wrong, please restart the game..")
        break
      computer_choice=random.choice(lis)
      if computer_choice==user_input:
        print("User Choice -> ",user_input,rps_dic[user_input])
        print("Computer Choice -> ",computer_choice,rps_dic[computer_choice])
        computer+=1
        user+=1
        print("Game Draw")
      elif user_input=="Rock" and  computer_choice=="Scissors" or user_input=="Paper" and  computer_choice=="Rock" or user_input=="Scissors" and  computer_choice=="Paper":        
        print("User Choice -> ",user_input,rps_dic[user_input])
        print("Computer Choice -> ",computer_choice,rps_dic[computer_choice])
        print("User Win 🤠")
        user+=1
      else:
        print("User Choice -> ",user_input,rps_dic[user_input])
        print("Computer Choice -> ",computer_choice,rps_dic[computer_choice])
        print("Computer Win 💻")
        computer+=1
    print("""
------- Final Result -------
""")    
    if computer==user:
      print("User Count = ",user)
      print("Computer Count = ",computer)
      print("Finally Game Draw.....")
    elif computer>user:
      print("User Count = ",user)
      print("Computer Count = ",computer)
      print("Finally Computer Win The Game.....") 
    elif computer<user:
      print("User Count = ",user)
      print("Computer Count = ",computer)
      print("Finally User Win The Game.....")   
  else:
    break