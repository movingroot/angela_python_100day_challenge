alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(_text, _shift, _direction) :
  _text = text
  # % for the case shift is larger than length of alphabet
  _shift = shift % len(alphabet) 
  _direction = direction.lower()
  message = ""
  # encode
  if _direction == 'encode' :
    for char in _text :
      position = alphabet.index(char)
      new_position = position + _shift
      if position < len(alphabet)-_shift :
        message += alphabet[new_position]
      # case when new_position is out of index
      else :
        message += alphabet[new_position-len(alphabet)]  
    print(f"The encoded text is {message}")
  # decode
  elif _direction == 'decode' :
    for char in _text :
      position = alphabet.index(char)
      original_position = position - _shift
      # case for out of index
      if position < _shift :
        message += alphabet[len(alphabet)+original_position]
      else :
        message += alphabet[original_position]  
    print(f"The decoded text is {message}")
  else :
    print("You entered the wrong direction.")

caesar(text, shift, direction)
