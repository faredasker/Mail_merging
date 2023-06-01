PLACEHOLDER = "[name]"

with open("./input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("./input/letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letters_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

