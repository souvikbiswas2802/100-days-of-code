from getpass import getpass as input
counter = 0;
P1Score = 0;
P2Score = 0;
print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move: (R for Rock, P for Paper or S for Scissors)")
while True:
  counter += 1
  print()
  if P1Score == 3:
    print("Player 1 wins the game!")
    break
  elif P2Score == 3:
    print("Player 2 wins the game!")
    break
  else:
    print("Round", counter)
    print()
    player1Move = input("Player 1 > ")
    player2Move = input("Player 2 > ")
    print()
    if player1Move=="R":
      if player2Move=="R":
        print("You both picked Rock, draw!")
        continue
      elif player2Move=="S":
        print("Player1 smashed Player2's Scissors into dust with their Rock!")
        P1Score += 1
      elif player2Move=="P":
        print("Player1's Rock is smothered by Player2's Paper!")
        P2Score += 1
      else:
        print("Invalid Move Player 2!")
        continue
    elif player1Move=="P":
      if player2Move=="R":
        print("Player2's Rock is smothered by Player1's Paper!")
        P1Score += 1
      elif player2Move=="S":
        print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
        P2Score += 1
      elif player2Move=="P":
        print("Two bits of paper flap at each other. Dissapointing. Draw.")
        continue
      else:
        print("Invalid Move Player 2!")
    elif player1Move=="S":
      if player2Move=="R":
        print("Player 2's Rock makes metal-dust out of Player1's Scissors")
        P2Score += 1
      elif player2Move=="S":
        print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
        continue
      elif player2Move=="P":
        print("Player1's Scissors make confetti out of Player2's paper!")
        P1Score += 1
      else:
        print("Invalid Move Player 2!")
        continue
    else:
      print("Invalid Move Player 1!")
