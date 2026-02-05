
#######################################################################
####################### File Encryption Module ########################
#######################################################################

import modules.languages as Languages
import modules.caesar as Caesar
import modules.vigenere as Vigenere

print("Loading File Module...")

encryption_key = None

def request_file():
    return input("""
#######################################################################
##                                                                   ##
##            Please enter the file directory:                       ##
##                                                                   ##
## ---------- Directory:  """)

def get_file_contents(path):
    contents = ""
    while True:
        try:
            with open(path, 'r') as input_file:
                contents += input_file.read()
            break
        except FileNotFoundError:
            print("""
#######################################################################
##                                                                   ##
##                      Error: File not found.                       ##
##                                                                   ##
#######################################################################
""")
            correction = request_file()
            contents = get_file_contents(correction)
            break
    return contents

def request_key():
    return input("""
#######################################################################
##                                                                   ##
##            Please enter your encryption key:                      ##
##                                                                   ##
## ---------- Key:  """)

def get_key_from_file():
    key_file_path = input("""
#######################################################################
##                                                                   ##
##            Please enter the path to                               ##
##            the file with encryption key:                          ##
##                                                                   ##
## ---------- Directory:  """)
    key = get_file_contents(key_file_path)
    return key

def request_key_preference():
    global encryption_key
    preference = input("""
#######################################################################
##                                                                   ##
##            Where is your key?                                     ##
##                                                                   ##
##            1. I will manually enter the key                       ##
##            2. My key is in a file                                 ##
##                                                                   ##
## ---------- Your preference:  """)
    match(preference):
        case '1':
            encryption_key = request_key()
        case '2':
            encryption_key = get_key_from_file()
        case _:
            print("""
                                 ------------------------------------##
##                                                                   ##
##                         Invalid Option.                           ##
##                           Returning...                            ##
##                                                                   ##
##--------------------------
""")
            request_key_preference()
            

def caesar_file_encrypt():
    file_to_encrypt = get_file_contents(request_file())
    print("""
#######################################################################
##                                                                   ##
##                           File contents:                          ##
##                                                                   ##

""")
    print(file_to_encrypt)
    request_key_preference()
    print("""
#######################################################################
##                                                                   ##
##                                Key:                               ##
##                                                                   ##

""")
    print(encryption_key)
    encrypted_contents = None
    while True:
        try:
            key = int(encryption_key)
            encrypted_contents = Caesar.caesar_encrypt(file_to_encrypt, key) 
            break
        except ValueError:
            print("\n##   Invalid key. Please make sure your key is strictly numerical.   ##\n\n")
            request_key_preference()
    print("""
#######################################################################
##                                                                   ##
##                  Below is your encrypted message:                 ##
##                                                                   ##
#######################################################################

""")
    print(encrypted_contents)
    save_output_in_file(encrypted_contents)

def caesar_file_decrypt():
    file_to_decrypt = get_file_contents(request_file())
    print("""
#######################################################################
##                                                                   ##
##                           File contents:                          ##
##                                                                   ##

""")
    print(file_to_decrypt)
    request_key_preference()
    print("""
#######################################################################
##                                                                   ##
##                                Key:                               ##
##                                                                   ##

""")
    print(encryption_key)
    decrypted_contents = None
    while True:
        try:
            key = int(encryption_key)
            encrypted_contents = Caesar.caesar_decrypt(file_to_decrypt, key) 
            break
        except ValueError:
            print("\n##   Invalid key. Please make sure your key is strictly numerical.   ##\n\n")
            request_key_preference()
    print("""
#######################################################################
##                                                                   ##
##                  Below is your decrypted message:                 ##
##                                                                   ##
#######################################################################

""")
    print(decrypted_contents)
    save_output_in_file(decrypted_contents)

def vigenere_file_encrypt():
    file_to_encrypt = get_file_contents(request_file())
    print("""
#######################################################################
##                                                                   ##
##                           File contents:                          ##
##                                                                   ##

""")
    print(file_to_encrypt)
    request_key_preference()
    print("""
#######################################################################
##                                                                   ##
##                                Key:                               ##
##                                                                   ##

""")
    print(encryption_key)
    encrypted_contents = Vigenere.vigenere_encrypt(file_to_encrypt, encryption_key) 
    print("""
#######################################################################
##                                                                   ##
##                  Below is your encrypted message:                 ##
##                                                                   ##
#######################################################################

""")
    print(encrypted_contents)
    save_output_in_file(encrypted_contents)

def vigenere_file_decrypt():
    file_to_decrypt = get_file_contents(request_file())
    print("""
#######################################################################
##                                                                   ##
##                           File contents:                          ##
##                                                                   ##

""")
    print(file_to_decrypt)
    request_key_preference()
    print("""
#######################################################################
##                                                                   ##
##                                Key:                               ##
##                                                                   ##

""")
    print(encryption_key)
    decrypted_contents = Vigenere.vigenere_decrypt(file_to_decrypt, encryption_key) 
    print("""
#######################################################################
##                                                                   ##
##                  Below is your decrypted message:                 ##
##                                                                   ##
#######################################################################

""")
    print(decrypted_contents)
    save_output_in_file(decrypted_contents)

def save_output_in_file(output_to_save):
    save_choice = input("""
#######################################################################
##                                                                   ##
##            Would you like to save the output in a file?           ##
##            (Warning: if you choose an existing file, contents     ##
##             will be overridden.)                                  ##
##                                                                   ##
##            1. Yes                                                 ##
##            2. No                                                  ##
##                                                                   ##
## ---------- Your preference:  """)

    match(save_choice):
        case '1':
            file_to_save = request_file()
            with open(file_to_save, 'w') as save_file:
                save_file.write(output_to_save)
            print("""
#######################################################################
##                                                                   ##
##            File saved at:                                         ##
##                                                                   ##
##            {path}
##                                                                   ##
#######################################################################
""".format(path = file_to_save))
        case '2': pass
        case _:
            print("""
                                 ------------------------------------##
##                                                                   ##
##                         Invalid Option.                           ##
##                           Returning...                            ##
##                                                                   ##
##--------------------------
""")
            save_output_in_file(output_to_save)



print("File Module loaded.")