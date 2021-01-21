direction =  input("Left or Right?\n").lower()
if direction != "left" :
  print("Fall into a hole. \nGame Over.")
else :
  direction = input("Swim or Wait?\n").lower()
  if direction != "wait" :
    print("Attacked by trout. \nGame Over.")
  else :
    direction = input("Which door? Red, Blue or Yellow?\n").lower()
    if direction == "red" :
      print("Burned by fire. \nGame Over.")
    elif direction == "blue" :
      print("Eaten by beasts. Game Over.")
    elif direction == "yellow" :
      print("You Win!")
    else :
      print("Game Over.")
