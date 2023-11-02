MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
  'C':'-.-.', 'D':'-..', 'E':'.',
  'F':'..-.', 'G':'--.', 'H':'....',
  'I':'..', 'J':'.---', 'K':'-.-',
  'L':'.-..', 'M':'--', 'N':'-.',
  'O':'---', 'P':'.--.', 'Q':'--.-',
  'R':'.-.', 'S':'...', 'T':'-',
  'U':'..-', 'V':'...-', 'W':'.--',
  'X':'-..-', 'Y':'-.--', 'Z':'--..',
  '1':'.----', '2':'..---', '3':'...--',
  '4':'....-', '5':'.....', '6':'-....',
  '7':'--...', '8':'---..', '9':'----.',
  '0':'-----', ', ':'--..--', '.':'.-.-.-',
  '?':'..--..', '/':'-..-.', '-':'-....-',
  '(':'-.--.', ')':'-.--.-'}


run_again = True

while run_again:
    morse_string = ""
    
    data_string = input("Enter the string you want convert to morse code: ").upper()

    for letter in data_string:
        morse_code = MORSE_CODE_DICT[letter]

        morse_string += morse_code

    print("The Morse code of given String: "+morse_string)

    type = input("Type something for do again. otherwise type 'no': ")
    if type == 'no':
        run_again = False
        print('bye')    
