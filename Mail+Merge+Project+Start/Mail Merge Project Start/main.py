with open("Input/Names/invited_names.txt") as invited_people:
    names = invited_people.readlines()

with open("Input/Letters/starting_letter.txt", "r") as letter_template:
    letter = letter_template.read()
    for i in names:
        cleaned_name = i.strip()
        new_letter = letter.replace("[name]", cleaned_name)
        with open(f"Output/ReadyToSend/letter_for_{cleaned_name}.txt", "w") as final:
            final.write(new_letter)


