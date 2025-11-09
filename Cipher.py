# Cipher.py
# This class will be responsible for encryption and decryption.
# Created Nov 5, 2025

# Cipher.py
# This class will be responsible for encryption and decryption.
# Created Nov 5, 2025

import csv 

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
        
        self._alphabet_upper += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # creates and stores latin uppercase alphabet 
        # string that contains all latin upper case letters 
        
        self._alphabet_lower += 'abcdefghijklmnopqrstuvwxyz'
        # creates and stores latin lower case alphabet
        # string that contains all latin lower case letters 
       
        self._case_sensitive = case_sensitive 
        # stores user preference for keeping same case as original text 
        # True = keep as original case 
        # False = convert to all uppercase upon encryption 

        self._history = []
        # creating history log attribute 
        # will store all encrypted and decrypted messages 
        # initializing it with empty list        

    def encrypt(self, message):
        '''Takes a plain-text message and returns an encrypted message.'''
        # defining method called encrypt for cipher class that takes one argument- message 
        # each letter shifts forward by __shifts
        # case sensitivity is decided based on user in _case_sensitive T/F selection

        encrypted = [] 
        # initializng empty list where encrytped message will go 
        
        for char in message: 
            # looping through each character in input message string
            # need to loop through each character individually to transform them 
        
            if char in self._alphabet_upper: 
                # checking if character is in upper case cyrillic or latin
                # checks against the string containing all upper case cyrillic self._alphabet_upper 
                # only want to apply encryption to cyrillic and latin characters, numbers, punctuation unchanged 
                
                index = self._alphabet_upper.index(char)
                # this finds the index position of upper case letter in message string 
                        
                new_index = (index + self.__shift) % len(self._alphabet_upper)
                # taking current index and calculating new index position with shift 
                # self.__shift, mangled attribute- the number of positions to move forward in alphabet 
                # adding shift to current position 
                # len gives total number of cyrillic and Latin alphabet upper case
                # modulus operator makes sure that the cipher stays in alphabet range determined by len
                # if end of alphabet is reached it will wrap back to beginning 
                        
                encrypted_char = self._alphabet_upper[new_index]
                # gets the encrypted version of the upper case character after calc new index position
                # using new_index position to retrieve new char from self._alphabet_upper string 
                # resulting char is set to encrypted_char for new letter that will go in final encrypted message 
                        
            elif char in self._alphabet_lower:  
                # checking if character is in lowercase cyrillic or latin if wasnt uppercase char
                # using self_alphabet_lower to compare against- contains all lowercase cyrillic or latin
                # will not change latin char, numbers, punctuation 

                index = self._alphabet_lower.index(char)
                # getting the index position of the lowercase cyrillic letter   

                new_index = (index + self.__shift) % len(self._alphabet_lower)
                # same process as the upper case but for lower case cyrillic letters 
                # calc new character after the shift 
                # gets length of alphabet- 33 and uses % to go to beginning of alphabet if goes past end  

                encrypted_char = self._alphabet_lower[new_index]
                # gets encrypted letter lower case from shifted index
                
            else:
                # if any letters not in cyrillic or latin
                # only encrypting Russian and latin messages 
                 
                encrypted_char = char
                # if not cyrillic or latin then character in message remains the same 
                # no change 
                         
            encrypted.append(encrypted_char)
            # adding all letters changed and unchanged to encrypted list
            # need the encrypted list to join characters together to form message 
                 
        encrypted_message = ''.join(encrypted)
        # combining all characters in encrypted list together in one string 
        # using .join to merge 
        
        if not self._case_sensitive:
            # if user decides no to case sensitive
            # user put False 
        
            encrypted_message = encrypted_message.upper()
            # will default to all upper case letters 
            # keeps it consistent since no original case was needed   
                
        self._history.append(("Зашифровать: (encrypt)", message, encrypted_message))
        # tracking the encryption process in a log 
        # "Encrypt" is the operation happening 
        # message- original message inputted 
        # encrypted_message - message after cipher completes 
        # double parenthesis because inner defines tuple
        # outer is for appending 
        
        return encrypted_message
        # returns final encrypted version of message to user 


    def decrypt(self, message):
        '''Takes an encrypted message and returns a plain text message. '''
        # defining method called decrypt for cipher class- takes one arg- message 
        # each letter will shift backwards by __shift
        # non cyrillic and latin alphabet characters remain as is/unchanged 
        # case sensitivity is decided based on user in _case_sensitive T/F selection

        decrypted = []
        # initializing empty list where decrypted characters will go

        for char in message:
            # looping through each individual character in message 

            if char in self._alphabet_upper:
                # checking if character is uppercase cyrillic or latin letter

                index = self._alphabet_upper.index(char)
                # getting the index of char in uppercase alphabet

                new_index = (index - self.__shift) % len(self._alphabet_upper)
                # shifting backward by __shift to get back to original char
                # uses % if shifting goes below 0/first letter in alphabet 
                # will wrap to end and keep shifting 

                decrypted_char = self._alphabet_upper[new_index]
                # getting original char from new_index  

            elif char in self._alphabet_lower:
                # checking if character is lowercase cyrillic or latin

                index = self._alphabet_lower.index(char)
                # getting index of letter in lower case alphabet 

                new_index = (index - self.__shift) % len(self._alphabet_lower)
                # calc new position after shifting backward by __shift 
                # uses % to wrap to end if shifting goes negataive 
                
                decrypted_char = self._alphabet_lower[new_index]
                # getting original character from new_index 

            else:
                # if any letters not in cyrillic or latin characters 
                # only encrypting Russian and Latin messags 
                 
                decrypted_char = char
                # if not cyrillic or latin then character in message remains the same 
                # no change

            decrypted.append(decrypted_char)
            # adding decrypted characters to decrypted list 
            # putting together message one letter at a time 
            # will also have to join characters for final message 

        decrypted_message = ''.join(decrypted)
        # joining all char into single string

        if not self._case_sensitive:
            # if self._case_sensitive is false 

            decrypted_message = decrypted_message.upper()
            # will convert the message to uppercase by default 

        self._history.append(("Расшифровать: (decrypt)", message, decrypted_message))
        # logs the decryption in _history list
        # Decrypt is what happened 
        # message is encrypted version 
        # decrypted_message is result/original message 

        return decrypted_message
        # returns original message
              
    def show_history(self):
        '''Displays the history of all encryption and decryption operations.'''
        # defining method in cipher class 
        # self gives access to _history because it is an attribute
        # will print record of each cipher operation

        for cipher_op, message, result in self._history:
            # loops through info stored in self._history
            # unpacking tuples into three variables 

            print(f"{cipher_op}:\n")
            # printing cipher operation ie- Encrypt or Decrypt 

            print(f" Сообщение: (message) {message}\n")
            # starting message that operation will be performed on 

            print(f" Результат: (result) {result}\n")
            # resulting message post cipher op completion 

            print("-" * 40)

    def save_history(self, filename = "cipher_history.txt"):
        '''Saves the history of all encryption and decryption operations to a text file.'''
        # defining method in Cipher class to save history to file
        # sets default filename to cipher_history.txt if user doesn't give different one 
        # self gives access to data and attributes for history 

        with open(filename, "w", encoding = "utf-8") as file:
            # opens file with name provided in filename 
            # with makes sure it properly closes afterwards 
            # "w" means write and create file or overwrite if already exists 
            # need the encoding utf-8 because of the cyrillic letters 
            # file is handle used for the opened/created file here

            for cipher_op, message, result in self._history:
                # loops through everything in the history list 
                # each item is a tuple of 3: 
                # cipher_op: encrypt or decrypt, message, result 

                file.write(f"{cipher_op}:\n")
                # writes operation type to the file 
                # \n goes to next line for formatting 

                file.write(f" Сообщение: (message) {message}\n")
                # writes message to file 

                file.write(f" Результат: (result) {result}\n\n")
                # writes result after encryption or decryption to file 

        print(f"История сохранена в файл: {filename}")
        print(f"History saved to file: {filename}")
        # confirmation messages
        
    def export_to_csv(self, filename = "cipher_history.csv"):
        '''Exports the encryption and decryption history to a CSV file.'''
        # defines method called export_to_csv inside the Cipher class 
        # takes one argument- filename 
            
        with open(filename, "w", newline ='', encoding = "utf-8") as file:
        # opens in write mode 
        # newline = '' will prevent extra blank lines in the spreadsheet 
        # need the utf-8 encoding to preserve Russian characters 
        # with closes file automatically after writing is completed 
        
            writer = csv.writer(file)
            # creating csv writer object 
          
            writer.writerow(["Operation", "Message", "Result"])
            # spreadsheet column names 
            
            for cipher_op, message, result in self._history:
            # going through the self._history list of tuples 
            # tuple = cipher_op, message, result 
            
                writer.writerow([cipher_op, message, result])
                # writing each tuple in the rows 
        
        print(f"История экспортирована в CSV: {filename}")
        print(f"History exported to CSV: {filename}")
        # confimration messages 
        
    def clear_history(self):
        '''Clears the encryption and decryption history.'''
        # defines method called clear_history in Cipher class

        self._history = []
        # this line essentially erases the history back to an empty list
        # will only erase history for current object not all objects in class 

        print("История очищена. History cleared.")
        # confirmation message
    
