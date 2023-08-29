import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetic)
nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_phonetic_alphabet_dict)


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        output = [nato_phonetic_alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
