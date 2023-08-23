# with open("input/Letters/starting_letter.txt") as letter:
#     invite_letter = letter.read()
#
#
# with open("input/Names/invited_names.txt") as names:
#     name_list = names.readlines()
#
# for name in name_list:
#     stripped_name = name.strip()
#     changed_sentence = invite_letter.replace("[name]", f"{stripped_name}")
#
#     with open(f"output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
#         file.write(f"{changed_sentence}")

PLACEHOLDER = "[name]"

with open("input/Names/invited_names.txt") as names_files:
    name_list = names_files.readlines()

with open("input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(f"output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
            file.write(new_letter)


