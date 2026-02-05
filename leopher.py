#######################################################################
############################# Leopher 3.1 #############################
#######################################################################
#         Project encrypts and decrypts messages according to         #
#                    Caesar and Vigenère Ciphers.                     #
#       Comments use British Spelling, do not spell-check them        #
#                      using American Spelling.                       #
#######################################################################


import modules.languages as Languages

print("Loading Cipher Algorithms...")

import modules.caesar as Caesar
import modules.vigenere as Vigenere

print("Cipher Algorithms loaded.")

import modules.filecrypt as Filecrypt


#######################################################################
########################### User Interface ############################
#######################################################################

def print_invalid_option():
  print("""
                             ----------------------------------------##
##                                                                   ##
##                         Invalid Option.                           ##
##                           Returning...                            ##
##                                                                   ##
##--------------------------
""")

def press_enter():
  input("""
                             ----------------------------------------##
##                                                                   ##
##                     Press enter to continue...                    ##
##                                                                   ##
##--------------------------
""")

def caesar_user_encrypt():
  print("""
#######################################################################
##                                                                   ##
##               Welcome to Caesar Encryption Service                ##
##                                                                   ##""")

  message = input("##                      Please enter your message:                   ##\n\n")
  key = 0
  encrypted_message = ""

  while True:
    user_input = input("\n\n##                   Please enter your encryption key:               ##\n\n")
    try:
      key = int(user_input)
      encrypted_message = Caesar.caesar_encrypt(message, key)      
      break    
    except ValueError:
      print("\n##   Invalid key. Please make sure your key is strictly numerical.   ##\n\n")

  print("""
#######################################################################
##                                                                   ##
##                  Below is your encrypted message:                 ##
##                                                                   ##
#######################################################################
  """)
  print(encrypted_message)
  top_menu()

def caesar_user_decrypt():
  print("""
#######################################################################
##                                                                   ##
##               Welcome to Caesar Decryption Service                ##
##                                                                   ##""")

  message = input("##                      Please enter your message:                   ##\n\n")
  key = 0
  decrypted_message = ""

  while True:
    user_input = input("\n\n##                   Please enter your encryption key:               ##\n\n")
    try:
      key = int(user_input)
      decrypted_message = Caesar.caesar_decrypt(message, key)   
      break       
    except ValueError:
      print("\n##   Invalid key. Please make sure your key is strictly numerical.   ##\n\n")

  print("""
#######################################################################
##                                                                   ##
##                  Below is your decrypted message:                 ##
##                                                                   ##
#######################################################################
""")
  print(decrypted_message)
  top_menu()

def vigenere_user_encrypt():
  print("""
#######################################################################
##                                                                   ##
##              Welcome to Vigenère Encryption Service               ##
##                                                                   ##""")
  message = input("##                      Please enter your message:                   ##\n\n")
  key = input("\n\n##                   Please enter your encryption key:               ##\n\n")
  encrypted_message = Vigenere.vigenere_encrypt(message, key)
  print("""
#######################################################################
##                                                                   ##
##                  Below is your encrypted message:                 ##
##                                                                   ##
#######################################################################
""")
  print(encrypted_message)
  top_menu()

def vigenere_user_decrypt():
  print("""
#######################################################################
##                                                                   ##
##              Welcome to Vigenère Decryption Service               ##
##                                                                   ##""")
  message = input("##                      Please enter your message:                   ##\n\n")
  key = input("\n\n##                   Please enter your encryption key:               ##\n\n")
  decrypted_message = Vigenere.vigenere_decrypt(message, key)
  print("""
#######################################################################
##                                                                   ##
##                  Below is your decrypted message:                 ##
##                                                                   ##
#######################################################################
""")
  print(decrypted_message)
  top_menu()


def top_menu():
  top_menu_choice = input("""
#######################################################################
##                                                                   ##
##            Please select the encryption algorithm:                ##
##                                                                   ##
##            1. Caesar                                              ##
##            2. Vigenère                                            ##
##                                                                   ##
##            OR:                                                    ##
##            9. Change Language of Encryption                       ##
##            0. Exit                                                ##
##                                                                   ##
## ---------- Your choice:  """)

  match(top_menu_choice):
    case '0': print("""
#######################################################################
##                                                                   ##
##                   Thank you for using Leopher!                    ##
##                            Exiting...                             ##
##                                                                   ##
#######################################################################
""")
    case '1': caesar_menu()
    case '2': vigenere_menu()
    case '9':
      Languages.language_menu()
      top_menu()
    case _:
      print_invalid_option()
      top_menu()

def caesar_user_input_menu():
  caesar_user_input_menu_choice = input("""
                             ----------------------------------------##
##                                                                   ##
##            Please select the Caesar operation:                    ##
##                                                                   ##
##            1. Encrypt                                             ##
##            2. Decrypt                                             ##
##            0. Change input source                                 ##
##                                                                   ##
## ---------- Your choice:  """)
  match(caesar_user_input_menu_choice):
    case '0': caesar_menu()
    case '1': caesar_user_encrypt()
    case '2': caesar_user_decrypt()
    case _:
      print_invalid_option()
      caesar_user_input_menu()    


def vigenere_user_input_menu():
  vigenere_user_input_menu_choice = input("""
                             ----------------------------------------##
##                                                                   ##
##            Please select the Vigenère operation:                  ##
##                                                                   ##
##            1. Encrypt                                             ##
##            2. Decrypt                                             ##
##            0. Change input source                                 ##
##                                                                   ##
## ---------- Your choice:  """)
  match(vigenere_user_input_menu_choice):
    case '0': vigenere_menu()
    case '1': vigenere_user_encrypt()
    case '2': vigenere_user_decrypt()
    case _:
      print_invalid_option()
      vigenere_user_input_menu()

def vigenere_menu():
  vigenere_menu_choice = input("""
                             ----------------------------------------##
##                                                                   ##
##            Where is your text source for the Vigenère operation?  ##
##                                                                   ##
##            1. I will manually enter the text                      ##
##            2. I want to import the text from a file               ##
##            0. Main Menu                                           ##
##                                                                   ##
## ---------- Your choice:  """)
  match(vigenere_menu_choice):
    case '0': top_menu()
    case '1': vigenere_user_input_menu()
    case '2': vigenere_file_input_menu()
    case _:
      print_invalid_option()
      vigenere_menu()

def caesar_menu():
  caesar_menu_choice = input("""
                             ----------------------------------------##
##                                                                   ##
##            Where is your text source for the Caesar operation?    ##
##                                                                   ##
##            1. I will manually enter the text                      ##
##            2. I want to import the text from a file               ##
##            0. Main Menu                                           ##
##                                                                   ##
## ---------- Your choice:  """)
  match(caesar_menu_choice):
    case '0': top_menu()
    case '1': caesar_user_input_menu()
    case '2': caesar_file_input_menu()
    case _:
      print_invalid_option()
      vigenere_menu()

def caesar_file_input_menu():
  caesar_file_input_menu_choice = input("""
                             ----------------------------------------##
##                                                                   ##
##            Please select the Caesar operation:                    ##
##                                                                   ##
##            1. Encrypt                                             ##
##            2. Decrypt                                             ##
##            0. Change input source                                 ##
##                                                                   ##
## ---------- Your choice:  """)
  match(caesar_file_input_menu_choice):
    case '0': caesar_menu()
    case '1':
      Filecrypt.caesar_file_encrypt()
      press_enter()
      top_menu()
    case '2':
      Filecrypt.caesar_file_decrypt()
      press_enter()
      top_menu()
    case _:
      print_invalid_option()
      caesar_file_input_menu()    


def vigenere_file_input_menu():
  vigenere_file_input_menu_choice = input("""
                             ----------------------------------------##
##                                                                   ##
##            Please select the Vigenère operation:                  ##
##                                                                   ##
##            1. Encrypt                                             ##
##            2. Decrypt                                             ##
##            0. Change input source                                 ##
##                                                                   ##
## ---------- Your choice:  """)
  match(vigenere_file_input_menu_choice):
    case '0': vigenere_menu()
    case '1':
      Filecrypt.vigenere_file_encrypt()
      press_enter()
      top_menu()
    case '2':
      Filecrypt.vigenere_file_decrypt()
      press_enter()
      top_menu()
    case _:
      print_invalid_option()
      vigenere_file_input_menu()


def main():
  print("""

     L        E E E E  O O O O  P P P    H     H  E E E E  P P P
     L        E        O     O  P     P  H     H  E        P     P
     L        E E E    O     O  P P P    H H H H  E E E    P P P
     L        E        O     O  P        H     H  E        P   P
     L L L L  E E E E  O O O O  P        H     H  E E E E  P     P

#######################################################################
############################ Leopher 3.1 ##############################
############################ theLionborn ##############################
############################# Feb  2026 ###############################
#######################################################################
#                                                                     #
#  Release Notes:                                                     #
#     - installation support                                          #
#                                                                     #
#######################################################################

Press enter to continue...
""")
  input()
  top_menu()

main()