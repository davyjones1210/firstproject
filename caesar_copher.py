import string

alphabets = string.ascii_lowercase
ask_continue = "yes"
cipher_text = ''
coded_letter = ''

def ask_encr(user_input, plain_text, shift_key):
    encrypted_text = ''
    decrypted_text = ''
    coded_letter = ''
    final_text=''

    if user_input == "encrypt":

        for letter in plain_text:
            #print(letter)
            index_letter = plain_text.index(letter)
            for i in range(0,26):
                if plain_text[index_letter] == alphabets[i]:
                    coded_letter = alphabets[(i + shift_key) % 26]
                    break
            else:
                coded_letter = " "
            encrypted_text = encrypted_text + coded_letter
    elif user_input == "decrypt":
        cipher_text = plain_text
        for letter in cipher_text:

            index_letter = cipher_text.index(letter)
            for i in range(0,26):
                if cipher_text[index_letter] == alphabets[i]:
                    decoded_letter = alphabets[(i - shift_key) % 26]
                    break
            else:
                decoded_letter = " "
            decrypted_text = decrypted_text + decoded_letter

    if user_input == "encrypt":
        print("Encrypted text is: ", encrypted_text)
    elif user_input == "decrypt":
        print("Decrypted text is: ", decrypted_text)


while ask_continue == "yes":
    user_input = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: ")
    plain_text = input("Type your message: ")
    shift_key = int(input("Type your shift key: "))
    ask_encr(user_input, plain_text, shift_key)
    ask_continue = input("Do you want to go again? yes or no:  ")

