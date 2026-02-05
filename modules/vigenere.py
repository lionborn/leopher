#######################################################################
########################### Vigenère Cipher ###########################
#######################################################################

print("Loading Vigenère Cipher Algorithm...")

#----------------------#
#   Cipher Algorithm   #
#----------------------#

import modules.languages as Languages
alphabet = Languages.alphabet

# Test if charachter is alphabetical

def is_alphabetical(character):
  if character in alphabet: return True, False # Alphabetical and lowercase
  elif character.lower() in alphabet: return True, True # Alphabetical and uppercase
  else: return False, False # Non-alphabetical

# Parse alphabetical-only text for key generation

def vigenere_parse_alphabetical(message):
  alphabetical_only = "" # Initialise the alphabetical-only string
  for i in range(len(message)): # For the entire message
    found = False # Flag for matches found
    for j in range(len(alphabet)): # Scan the entire global alphabet variable for matches
      if message[i] == alphabet[j]: # If match found
        alphabetical_only += message[i] # Add it to the alphabetical-only string
        found = True # Flag it up
        break # Break the inner loop
      elif message[i].lower() == alphabet[j]: # If capitalised match found
        alphabetical_only += message[i].upper() # Add capitalised character to the alphabetical-only string
        found = True # Flag it up
        break # Break the inner loop
      else: continue # If not, continue
    if found == False: continue # If after the search, no alphabetical character found, skip
  return alphabetical_only # Return the alphabetical only string 

# Generate an alphabetical Vigenère key to the alphabetical message length

def vigenere_alphabetical_key(full_message, key_raw):

  message = vigenere_parse_alphabetical(full_message) # Convert the full message to alphabetical-only string
  key = vigenere_parse_alphabetical(key_raw) # Make sure to eliminate non-alphabetical characters from the key

  full_length_key = "" # Initialise full length key string
  message_length = len(message) # Store message length
  key_length = len(key) # Store key length
  repetition_quotient = 0 # Initialise a quotient for repetition of the key

  if message_length == key_length:
    full_length_key += key # If message length equals key length, simply store the key as it is
  elif message_length < key_length:
    full_length_key += key[:message_length] # If message length is less than key length, trim the key to message length
  elif message_length > key_length and message_length % key_length == 0:
    repetition_quotient = int(message_length / key_length)
    for i in range(repetition_quotient):
      full_length_key += key # If message length is greater than and divisible by key length, then save the division result to quotient and repeat the key as many as the quotient
  elif message_length > key_length and message_length % key_length != 0:
    repetition_quotient = int(message_length / key_length)
    key_remainder = key[:(message_length % key_length)]
    for i in range(repetition_quotient):
      full_length_key += key
    full_length_key += key_remainder # If message length is greater than and NOT divisible by key length, then save the division result to quotient and repeat the key as many as the quotient, add the clipped key to the remaining spaces as necessary 

  return full_length_key # Return the key to the length of the message

# Vigenère Numerical Key

def vigenere_numerical_key(message, key):
  alphabetical_key = vigenere_alphabetical_key(message, key) # Convert key to full-lenght alphabetical key
  numerical_key = [] # Initialise numerical key list
  for char in alphabetical_key: # Iterate through the alphabetical key
    if char in alphabet: # If character found in the alphabet
      numerical_key.append(alphabet.index(char)) # Find each character's global alphabet variable index and store it in the numerical key list
    elif char.lower() in alphabet: # If capitalised character found in the alphabet
      numerical_key.append(alphabet.index(char.lower())) # Find lowercase version of character in the global alphabet variable, store its index in the numerical key list
  return numerical_key # Return numerical key list

# Vigenère Decryption Algorithm

def vigenere_decrypt(message, key):

  global alphabet
  alphabet = Languages.alphabet

  vigenere_key = vigenere_numerical_key(message, key) # Generate the numerical key for the message
  decrypted_message = "" # Initialise the decrypted message script
  key_index = 0 # Define a different index for key since the key ommits the non-alphabetical characters
  for i in range(len(message)): # Iterate through the length of the message
    if is_alphabetical(message[i]) == (True, False): # Test to see if the character at hand is alphabetical and lowercase
      initial_index = alphabet.index(message[i]) # Find the alphabetical index of the character at hand
      shifted_index = initial_index + vigenere_key[key_index] # Shift the index of the character based on the key
      if shifted_index >= len(alphabet): shifted_index -= len(alphabet) # Adjust the index if overflows the length of the alphabet
      decrypted_message += alphabet[shifted_index] # Add the alphabetical character to the decrypted message based on the index
      key_index += 1 # Increase the key index due to alphabetical processing
    elif is_alphabetical(message[i]) == (True, True): # Test to see if the character at hand is alphabetical and uppercase
      initial_index = alphabet.index(message[i].lower()) # Find the alphabetical index of the character at hand
      shifted_index = initial_index + vigenere_key[key_index] # Shift the index of the character based on the key
      if shifted_index >= len(alphabet): shifted_index -= len(alphabet) # Adjust the index if overflows the length of the alphabet
      decrypted_message += alphabet[shifted_index].upper() # Add the capitalised alphabetical character to the decrypted message based on the index
      key_index += 1 # Increase the key index due to alphabetical processing
    else:
      decrypted_message += message[i] # If not alphabetical character, add the character as-is to the decrypted message 
  return decrypted_message # Return decrypted message string

# Vigenère Encryption Algorithm

def vigenere_encrypt(message, key):

  global alphabet  
  alphabet = Languages.alphabet

  vigenere_key = vigenere_numerical_key(message, key) # Generate the numerical key for the message
  encrypted_message = "" # Initialise the encrypted message script
  key_index = 0 # Define a different index for key since the key ommits the non-alphabetical characters
  for i in range(len(message)): # Iterate through the length of the message
    if is_alphabetical(message[i]) == (True, False): # Test to see if the character at hand is alphabetical and lowercase
      initial_index = alphabet.index(message[i]) # Find the alphabetical index of the character at hand if alphabetical
      shifted_index = initial_index - vigenere_key[key_index] # Shift the index of the character based on the key
      if shifted_index >= len(alphabet): shifted_index -= len(alphabet) # Adjust the index if overflows the length of the alphabet
      encrypted_message += alphabet[shifted_index] # Add the alphabetical character to the encrypted message based on the index
      key_index += 1 # Increase the key index due to alphabetical processing
    elif is_alphabetical(message[i]) == (True, True):
      initial_index = alphabet.index(message[i].lower()) # Find the alphabetical index of the character at hand if alphabetical and upeercase
      shifted_index = initial_index - vigenere_key[key_index] # Shift the index of the character based on the key
      if shifted_index >= len(alphabet): shifted_index -= len(alphabet) # Adjust the index if overflows the length of the alphabet
      encrypted_message += alphabet[shifted_index].upper() # Add the capitalised alphabetical character to the encrypted message based on the index
      key_index += 1 # Increase the key index due to alphabetical processing
    else:
      encrypted_message += message[i] # If not alphabetical character, add the character as-is to the encrypted message 
  return encrypted_message # Return encrypted message string

print("Vigenère Cipher Algorithm loaded.")

