# by: Prathyusha Theerdhala
import random
from time import sleep
choice = ["Rock", "Paper", "Scissors"]
computer = random.choices(choice)
player = False
while player == False:
  print("Welcome to Rock,Paper and Scissors")
  print("\nPlease wait...The game is loading....")
  sleep(3)
  player = input("You have 4 options: \n'Rock': 'Rock'\n'Paper': 'Paper'\n'Scissors': 'Scissors'\n'Stop the game': 'Stop':\n Which one do you want to choose?")
  if player == computer:
    print("\nPlease wait...You will be able to see your result in a few seconds...")
    sleep(2)
    print("It's a Tie! The computer also chose", player)
    print("Run the program again to play!")
  elif player == "Rock":
    if computer == "Paper":
      print("\nPlease wait...You will be able to see your result in a few seconds...")
      sleep(2)
      print("Sorry!You have lost! The computer chose Paper!")
      print("Run the program again to play!")

    else:
      print("\nPlease wait...You will be able to see your result in a few seconds...")
      sleep(2)
      print("Hurray!You have won! The computer chose Scissors!")
      print("Run the program again to play!")

  elif player == "Paper":
      if computer == "Rock":
        print("\nPlease wait...You will be able to see your result in a few seconds...")
        sleep(2)
        print("Hurray!You have won! The computer chose Rock!")
        print("Run the program again to play!")

      else:
        print("\nPlease wait...You will be able to see your result in a few seconds...")
        sleep(2)
        print("Sorry!You have lost! The computer chose Scissors")
        print("Run the program again to play!")

  elif player == "Scissors":
      if computer == "Paper":
        print("\nPlease wait...You will be able to see your result in a few seconds...")
        sleep(2)
        print("Hurray!You have won! The computer chose Paper")
        print("Run the program again to play!")

      else:
        print("\nPlease wait...You will be able to see your result in a few seconds...")
        sleep(2)
        print("Sorry!You have lost! The computer chose Rock")
        print("Run the program again to play!")

  elif player == "Stop":
      print("Thanks for playing!")
      break
  else:
      print("That's not a valid choice!Please run the program again to play.Thank You!")
      break
player = False
