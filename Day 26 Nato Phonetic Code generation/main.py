import pandas


# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetic)

nato_phonetic_alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_phonetic_alphabet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output = [nato_phonetic_alphabet_dict[letter] for letter in user_input]

print(output)


# list_phonetic_code = []
# for letter in user_input:
#
#     for (phonetic, code) in nato_phonetic_alphabet_dict.items():
#         if phonetic == letter:
#             list_phonetic_code.append(code)
#
# print(list_phonetic_code)
