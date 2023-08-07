alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  elif cipher_direction == "encode":
    shift_amount *= 1
  else:
    print("wrong input")
  for char in start_text:
    
    if char in alphabet:
      
    
      position = alphabet.index(char)
      new_position = position + shift_amount  
      end_text += alphabet[new_position]
    else:
      end_text += char
  if cipher_direction == "encode" or cipher_direction == "decode":  
    print(f"Here's the {cipher_direction}d result: {end_text}")
  else:
    print("please input encode or decode")

from art import logo
print(logo)


run_again = True
while run_again:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  type = input("Type 'yes' if yoy want to go again. Otherwise type 'no'.\n")
  print("\n")
  if type == 'no':
    run_again = False
    print("Good bye")  
