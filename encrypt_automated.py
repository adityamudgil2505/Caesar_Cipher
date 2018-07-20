# Variables
# we need to store alphabets
# need to store numbers
# need to store message
# need to store encrpted message
# need to enter key which should be known to both sender and reciever

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
# message = 'I love programming'
message = input('Enter your message\n')
encryted_message = ''
key = 3
message = message.upper()
for character in message:
    if character in alphabets:
        curr_position = alphabets.find(character)
        new_position = (curr_position + key) % 26
        new_character = alphabets[new_position]

    elif character in numbers:
        curr_position = numbers.find(character)
        new_position = (curr_position + key) % 10
        new_character = numbers[new_position]

    else:
        new_character = character
    encryted_message += new_character

print('Your encrypted message is\n'+encryted_message)