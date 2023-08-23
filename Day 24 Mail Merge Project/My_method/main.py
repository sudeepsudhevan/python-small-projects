with open("input/Letters/starting_letter.txt") as letter:
    invite_letter = letter.readlines()
    later = ''.join([str(elem) for elem in invite_letter[1:]])

# print(invite_letter)
# print(invite_letter[1:])

with open("input/Names/invited_names.txt") as names:
    name_list = names.readlines()
print(name_list)
for name in name_list:
    stripped_name = name.strip()
    changed_sentence = invite_letter[0].replace("[name]", f"{stripped_name}")
    # print(changed_sentence)

    with open(f"output/ReadyToSend/letter_for_{stripped_name}", mode="w") as file:
        file.write(f"{changed_sentence}{later}")
