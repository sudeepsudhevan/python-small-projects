with open("input/Letters/starting_letter.txt") as letter:
    invite_letter = letter.read()


with open("input/Names/invited_names.txt") as names:
    name_list = names.readlines()

for name in name_list:
    stripped_name = name.strip()
    changed_sentence = invite_letter.replace("[name]", f"{stripped_name}")

    with open(f"output/ReadyToSend/letter_for_{stripped_name}", mode="w") as file:
        file.write(f"{changed_sentence}")
