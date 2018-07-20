# how to hack Caeser Cipher
# we use brute force to iterate over all the possible keys i.e, form 1 to 27
def hack(encryted_message,key):
    capital_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_alphabets = capital_alphabets.lower()
    numbers = '1234567890'
    # message = 'vgvgGVGDFI565'
    message = ''
    for character in encryted_message:
        if character in capital_alphabets:
            curr_position = capital_alphabets.find(character)
            new_position = (curr_position - key) % 26
            new_character = capital_alphabets[new_position]

        elif character in small_alphabets:
            curr_position = small_alphabets.find(character)
            new_position = (curr_position - key) % 26
            new_character = small_alphabets[new_position]

        elif character in numbers:
            curr_position = numbers.find(character)
            new_position = (curr_position - key) % 10
            new_character = numbers[new_position]

        else:
            new_character = character
        message += new_character
    return message

encrypted_messag = input('Enter Encrypted message\n')
for i in range(1,27):
    print(hack(encrypted_messag,i))
