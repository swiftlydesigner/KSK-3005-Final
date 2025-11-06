# Cipher.py
# This class will be responsible for encryption and decryption.
# Created Nov 5, 2025

class Cipher:
    # defining cipher class for encryption and decryption
    # blueprint for creating Cipher objects that performs two functions: 
        # Encrypt text by shifting letters forward in the alphabet
        # Decrypt by shifting letters backward to get to original message 
    '''
        Attributes:
            # __shift (int): Number shifts for each letter
            # _alphabet_upper (str): uppercase Russian alphabet
            # _alphabet_lower (str): lowercase Russian alphabet
            # _case_sensitive (bool): gives option to keep original case or put all in upper after encrypting 
            # _history (list): keeps record of all encrypted/decrypted messages 
     '''
    
    def __init__(self, shift = 3, case_sensitive = True):
        # the construction method that will happen everytime there is new cipher object
        # initializing cipher attributes 
                
        self.__shift = shift
            # creating the attribute called __shift and storing shift value
            # self. attaches the number of shifts to the current cipher object
            # __ means this attribute's name is mangled/extra private
            # shift gets assigned number inputted by user
                 
        self._alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' 
            # creates and stores Russian _alphabet_upper 
            # string that contains all cyrillic upper case letters 
            # _ makes it private
         
        self._alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя' 
            # creates and stores Russian lowercase alphabet
            # string that contains all cyrillic lower case letters 
       
        self._case_sensitive = case_sensitive 
            # stores user preference for keeping same case as original text 
            # True = keep as original case 
            # False = convert to all uppercase upon encryption 

        self._history = []
            # creating history log attribute 
            # will store all encrypted and decrypted messages 
            # initializing it with empty list        

    '''
        Note to coders: Only use private or mangled methods. The only public methods should be encrypt or decrypt. All methods must start with one or two underscores.
        Private method: _my_private method (starts with one _)
            - Use for methods you do not mind being seen outside of this class, but prohibit them from calling it.
        Mangled method: __my_mangled method (starts with two _)
            - Use for methods that you do not want to be visible outside of this class, ever.
    '''

    def encrypt(self, message):
        '''
            Takes a plain-text message and returns an excrypted message.
        '''
        pass # Encrypt and return a string here

    def decrypt(self, message):
        '''
            Takes an encrypted message and returns a plain text message.
        '''
        pass # Decrypt and return a string here
