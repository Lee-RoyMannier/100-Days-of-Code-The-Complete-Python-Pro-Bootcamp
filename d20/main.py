# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


file = open("Input/Names/invited_names.txt", "r")
names = file.readlines()
file.close()

exemple_file = open("Input/Letters/starting_letter.txt", "r")
exemple = exemple_file.readlines()
exemple_file.close()

for name in names:
    namestrip = name.strip()
    with open(f"Output/ReadyToSend/{name}.txt", "w") as file:
        for ex in exemple:
            ex = ex.replace("[name]", namestrip)
            file.write(ex)
