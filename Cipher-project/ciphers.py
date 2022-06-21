def get_dictionaries():
    """
    Generates two dicitonaris- letter_dict where the keys are the letters of the alphabet and the values are 0 to 26,
    and number_dict where the keys are 0 to 26 and the values are the letters of the alphabet. 
    """
    letter_dict = {}  # keys are letters
    number_dict = {}  # keys are numbers
    a = ord('a')

    for i in range(26):
        letter_dict[chr(i + a)] = i
        number_dict[i] = chr(i + a)

    return letter_dict, number_dict

def get_new_letter(letter, offset, shift_right, letter_dict, number_dict):
    """
    Returns a new letter based on the offset number and direction. Requires a letter (str), offset (int), shift_right (bool),
    and the two dictionaries from the get_dictionaries function.
    """
  
    key_number = letter_dict[letter]
    
    if shift_right:
        new_key_number = (key_number + offset) % 26
    else:
        new_key_number = (key_number - offset) % 26
    
    return number_dict[new_key_number]

def caeser_cipher(message, offset, shift_right):
    """
    Codes or decodes a message based on the caesar cipher. Takes each letter in a message and codes it my an offset and 
    direction. To decode, use the same offset and the opposite direction. Requirments: message (str), offset (int), and 
    shift_right (bool). If shift_right is True, the message will be coded in the positive direction and visa versa.
    """
    letter_dict, number_dict = get_dictionaries()
    new_letter = get_new_letter  # assign the function for getting the letter to a variable
    new_message = []
    message = message.lower()
    for letter in message:
        if letter.isalpha():
            letter = new_letter(letter, offset, shift_right, letter_dict, number_dict)
        new_message.append(letter)

    return ''.join(new_message) 
  
def vigenere_cipher(message, keyword, shift_right):
    """
    Codes or decodes a message based on the vigenere cipher. Takes each letter in a message and codes it my an offset and 
    direction. The offset is a keyword and each letter will be shifted based on the value of the letters in the keyword.
    The keyword repeats itelf to obtain values to shift until the mesage has been completely coded. To decode, use the same 
    keyword and the opposite direction. Requirments: message (str), offset (str), and shift_right (bool). 
    If shift_right is True, the message will be coded in the positive direction and visa versa.
    """
    letter_dict, number_dict = get_dictionaries()
    
    cipher = []
    keyword = keyword.lower()
    for letter in keyword:
        cipher.append(letter_dict[letter])
    
    new_message = []
    count = 0
    keyword_length = len(cipher)
    new_letter = get_new_letter  # assign the function for getting the letter to a variable
    
    message = message.lower()
    for letter in message:
        if letter.isalpha():
            letter = new_letter(letter, cipher[count], shift_right, letter_dict, number_dict)
            count = (count + 1) % keyword_length
        
        new_message.append(letter)
    
    return ''.join(new_message)