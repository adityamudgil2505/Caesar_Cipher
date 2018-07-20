# Variables
# we need to store alphabets
# need to store numbers
# need to store message
# need to store encrpted message
# need to enter key which should be known to both sender and reciever

capital_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_alphabets = capital_alphabets.lower()
numbers = '1234567890'
# message = 'I love programming'
message = input('Enter your message\n')
encryted_message = ''
key = 3
for character in message:
    if character in capital_alphabets:
        curr_position = capital_alphabets.find(character)
        new_position = (curr_position + key) % 26
        new_character = capital_alphabets[new_position]

    elif character in small_alphabets:
        curr_position = small_alphabets.find(character)
        new_position = (curr_position + key) % 26
        new_character = small_alphabets[new_position]

    elif character in numbers:
        curr_position = numbers.find(character)
        new_position = (curr_position + key) % 10
        new_character = numbers[new_position]

    else:
        new_character = character
    encryted_message += new_character

print('Your encrypted message is\n'+encryted_message)