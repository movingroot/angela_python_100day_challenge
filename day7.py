stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# set pre-game
chosen_word = input("Write the word for playing hangman!\n: ")
word_length = len(chosen_word)
lives = 6

# Game setting
display = []
for _ in range(word_length):
    display += "_"
print(display)
print(stages[lives])

# Game Start

is_won = False
is_over = False

while not is_won and not is_over :
  cnt = 0
  guess = input("\n\nGuess a letter: ").lower()


  for i in range(word_length) :
    if guess == chosen_word[i] :
      display[i] = chosen_word[i]
      cnt += 1
  
  # guess in chosen_word?
  # if yes, continue
  # if not, life -1
  if cnt == 0 :
    lives -= 1
    print(stages[lives])
    print(display)
  else :
    print(display)

  # game over or not
  if lives >= 0 :
    is_over = False
  else :
    is_over = True

  # win or not
  if "_" not in display :
    is_won = True
  else :
    is_won = False

# after while loop gets broken
if is_won == True :
  print("You won!")

if is_over == True :
  print("You lose!")
