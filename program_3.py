# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
def word_separator(sentence):
    new_sentence = ""

    for index, char in enumerate(sentence):
        if char.isupper() and index != 0:
            new_sentence += " "
        new_sentence += char.lower()


    new_sentence = new_sentence[0].upper() + new_sentence[1:]

    if not new_sentence.endswith((".", "!", "?")):
        new_sentence += "."

    return new_sentence



camel_case_input = input("Enter a CamelCase sentence: ")
separated_sentence = word_separator(camel_case_input)
print(separated_sentence)