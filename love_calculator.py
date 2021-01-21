"""
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
"""

combine = name1 + name2
toSum1 = 0
toSum2 = 0

for i in combine :
  if i == "T" or i == "R" or i == "U" or i == "E" or i == "t" or i == "r" or i == "u" or i == "e" :
    toSum1 += 1
  else :
    toSum1 += 0

for j in combine :
  if j == "L" or j == "O" or j == "V" or j == "E" or j == "l" or j == "o" or j == "v" or j == "e" :
    toSum2 += 1
  else :
    toSum2 += 0

score = toSum1*10 + toSum2

if score<10 or score>90 :
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50 :
  print(f"Your score is {score}, you are alright together.")
else :
  print(f"Your score is {score}.")
  

# clear approach
combine = (name1 + name2).lower()

t = combine.count("t")
r = combine.count("r")
u = combine.count("u")
e = combine.count("e")
l = combine.count("l")
o = combine.count("o")
v = combine.count("v")

score = (t + r + u + e)*10 + (l + o + v + e)

if score<10 or score>90 :
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50 :
  print(f"Your score is {score}, you are alright together.")
else :
  print(f"Your score is {score}.")
