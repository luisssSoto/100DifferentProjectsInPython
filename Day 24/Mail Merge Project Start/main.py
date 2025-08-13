#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt", "r") as guests_file:
    guests = guests_file.readlines()
print(guests)

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter = letter_file.read()
print(letter)

def write_letters(guests_list, type_letter):
    for guest in guests_list:
        guest = guest.strip()
        with open(f"./Output/ReadyToSend/letter_for_{guest}.txt", "w") as guest_letter:
            edited_letter = type_letter.replace("[name]", guest)
            guest_letter.write(edited_letter)

write_letters(guests, letter)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp