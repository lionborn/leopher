
#######################################################################
############################## Languages ##############################
#######################################################################

print("Loading Languages...")

available_languages = {
  'en': {
    'iso-code': 'en',
    'language-string': 'English',
    'alphabet': "abcdefghijklmnopqrstuvwxyz"
  },
  'tr': {
    'iso-code': 'tr',
    'language-string': 'Turkish (Türkçe)',
    'alphabet': "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
  },
  'ru': {
    'iso-code': 'ru',
    'language-string': 'Russian (Русский)',
    'alphabet': "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
  },
  'ar': {
    'iso-code': 'ar',
    'language-string': 'Arabic (العربية)',
    'alphabet': "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
  },
  'he': {
    'iso-code': 'he',
    'language-string': 'Hebrew (עברית)',
    'alphabet': "אבגדהוזחטיכלמנסעפצקרשת"
  },
  'sq': {
    'iso-code': 'sq',
    'language-string': 'Albanian (Shqip)',
    'alphabet': "abcçdeëfghijklmnopqrstuvwxyz"
  },
  'sr': {
    'iso-code': 'sq',
    'language-string': 'Serbian (Latin) (Srpski)',
    'alphabet': "abcčćdđefghijklmnoprsštuvzž"
  }
}

#----------------------#
#  Language Mechanism  #
#----------------------#

# Class Language for the language dictionary above

class Language:
  def __init__(self, lang = 'en'):
    chosen_language = available_languages.get(lang)
    self.iso_code = chosen_language.get('iso-code')
    self.language_string = chosen_language.get('language-string')
    self.current_alphabet = chosen_language.get('alphabet')

  def __repr__(self):
    return """

#######################################################################
##                                                                   ##
##                          Language in Use:                         ##
##                                                                   ##
                            {lang_str}
##                                                                   ##
##                                                                   ##
#######################################################################
""".format(lang_str = self.language_string)

  def change_language(self, lang):
    chosen_language = available_languages.get(lang)
    self.iso_code = chosen_language.get('iso-code')
    self.language_string = chosen_language.get('language-string')
    self.current_alphabet = chosen_language.get('alphabet')
    update_alphabet()

language_in_use = Language()

alphabet = [] # The alphabet as global variable

def update_alphabet():
  global alphabet
  alphabet = language_in_use.current_alphabet

update_alphabet()

def language_menu():
  user_language_choice = input("""
#######################################################################
##                                                                   ##
##            Please select the encryption language:                 ##
##                                                                   ##
##            1. English (Default)                                   ##
##            2. Turkish (includes 'Q', 'X', 'W')                    ##
##            3. Albanian (includes 'W')                             ##
##            4. Serbian (Latin)                                     ##
##            5. Russian                                             ##
##            6. Arabic                                              ##
##            7. Hebrew                                              ##
##                                                                   ##
##            OR:                                                    ##
##                                                                   ##
##            0. Do NOT change the language                          ##
##               and return to the main menu                         ##
##                                                                   ##
## ---------- Your choice [Current Language: {lang}]:  """.format(lang = language_in_use.language_string))
  match(user_language_choice):
    case '1':
      language_in_use.change_language('en')
      print(language_in_use)
    case '2':
      language_in_use.change_language('tr')
      print(language_in_use)
    case '3':
      language_in_use.change_language('sq')
      print(language_in_use)
    case '4':
      language_in_use.change_language('sr')
      print(language_in_use)
    case '5':
      language_in_use.change_language('ru')
      print(language_in_use)
    case '6':
      language_in_use.change_language('ar')
      print(language_in_use)
    case '7':
      language_in_use.change_language('he')
      print(language_in_use)
    case '0':
      pass
    case _:
      print_invalid_option()
      language_menu()

print("Languages loaded.")