
def caesar_cipher(ciphertext, shift):
    ciphertext = ciphertext.lower() #converts entered ciphertext to lowercase
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = '' #initialises plaintext to an empty string


    if shift and type(shift) == int :#begin decryption if the shift entered is a number
        for i in ciphertext:
            
            if i in alphabet:
                index = alphabet.index(i)
                new_position = (index - shift) % 26 
                plaintext += alphabet[new_position]
                
            elif i == ' ':
                plaintext += ' '
                
            else:
                plaintext += i #in case character in plaintext is not found in alphabet, it ignores
                                #it and moves to the next character
        return plaintext
    
#2 of exercise 1 code: obtaining key without human key verification - brute force 
#Code inspiration was gotten from https://inventwithpython.com/cracking/chapter6.html

    elif shift == None: #as no shift(key) is supplied, the code loops through all possible shifts
                        #index 0 - 25 
        for shift in range(len(alphabet)):
            plaintext = ' '

            for i in ciphertext:
                if i in alphabet:
                    index_i = alphabet.index(i)
                    plaintext_index = index_i - shift

                    if plaintext_index < 0: 
                        plaintext_index += len(alphabet)

                    plaintext += alphabet[plaintext_index]

                else:
                    plaintext += i

            print('Shift{}: {}'.format(shift, plaintext)) #result of all possible shifts

            #presents user with an error message about the entered shift
    else: 
        return ('Invalid Shift format entered. Shift should be a number(of type int) or "None". ')

      


''' Suggested ways to improve the code.
1. Automatically make the code move the shifts in a predefined sequence.
2. Read from file.
3. Handle Case '''
