import random
import string

def generate_password(mini_length, numbers=True, special_characters=True): #conditions
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    #password variables
    pw = "" #passsword
    meets_criteria = False
    has_numbers = False
    has_special = False


    while not meets_criteria or len(pw) < mini_length: #condition to check if it meets the criteria
        new_char = random.choice(characters)
        pw += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pw


def repeat(min_length, has_numbers, has_special): #ask if the user wants to generate a new password
    while True:
        answer = input("Would you like to generate a new password? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            min_length = int(input("Enter the new amount:")) #define new length
            has_numbers = input("Do you want to have numbers in your new password? (y/n):").lower() == "y" #request for numbers
            has_special =  input("Do you want any special characters added? (y/n):").lower() == "y" #request for special characters
            pw = generate_password(min_length, has_numbers, has_special) #generate again
            print("The new generated password is:", pw) #results
        elif answer in ("n", "no"):
            print("See you next time!")
            return False

min_length = int(input("Enter the amount of characters you want in your password: ")) #define the length of the password
has_numbers = input("Do you want to have numbers in your password? (y/n):").lower() == "y" #request user input for numbers
has_special = input("Do you want any special characters added? (y/n):").lower() == "y" #request user input for special characters

pw = generate_password(min_length, has_numbers, has_special) #generate
print("The generated password is:", pw) #results

if not repeat(min_length, has_numbers, has_special): #if user doesnt request new password
    print("Thank you for using the password generator!")
