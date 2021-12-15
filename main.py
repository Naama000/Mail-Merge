#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as names:
    names = names.read().splitlines()

    for name in names:
        with open("./Input/Letters/starting_letter.txt", "r") as original:
            new_mail = original.read()
            new_mail = new_mail.replace("[name]", name)

        with open(f"./Output/ReadyToSend/Letter_for_{name}.txt", mode="w") as new_letter:
            new_letter.write(new_mail)

