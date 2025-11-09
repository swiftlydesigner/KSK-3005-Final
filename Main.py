# Koa Hawn
# Sarah Tillman
# Kyle Parker

# Final Project - 3005
# Autumn Quarter 2025
# Due Nov 14, 2025

# Created Nov 5, 2025
# Modified Nov 5, 2025

import Cipher
# importing the cipher.py file for use that is in same directory 
# the cipher file contains class- Cipher with two methods: encrypt, decrypt 

def main():
    # defining function called main 
    # it is the function where the cipher programs logic will run 
    
    cipher = Cipher.Cipher(shift = 5, case_sensitive = True)
    
    # this initializes a new Cipher object/instance of the Cipher class 
    # assign and store it to a variable called cipher 
    
    # Cipher.Cipher means access that file that contains the class
    # Cipher() - calls constructor of the class to create new object
    
    # full lines means to create a new instance/object based on the blueprint class in Cipher.py
    # stored it in new variable called cipher to run encrypt/decrypt operations 
    
    
    preset_messages_pairs = [
        ("Кто не рискует, тот не пьет шампанского", "He who doesn't take risks doesn't drink champagne")
        ("Работа не волк— в лес не убежит." , "Work isn't a wolf- it won’t run away into the forest.")
        ("Слово не воробей: вылетит — не поймаешь", "A word is not a sparrow: once it flies out, you won’t catch it.") 
        ("двумя зайцами погонишься, ни одного не поймаешь." , "If you chase two hares, you will not catch either.")
        ("Без труда не вытащишь и рыбку из пруда." , "Without effort, you won’t even pull a fish out of a pond.")
        ("Авось да небось до добра не доведут." , "Maybe and perhaps, won’t lead to any good." )
        ("Доверяй, но проверяй." , "Trust but verify.")
        ("Что посеешь, то и пожнёшь." , "You reap what you sow.")
        ("В тихом омуте черти водятся.", "Still waters run deep with devils")
        ("Не всё то золото, что блестит." , "Not all that glitters is gold.")
        ("Повторение — мать учения." , "Repetition is the mother of learning.")
        ("Не попробуешь — не узнаешь" , "If you don’t try, you’ll never find out.")
        
    ]

    while True:
            
        print("--------------------------------------")
        print(" ***** Меню Шифра / Cipher Menu ***** " )
        print("--------------------------------------\n")
        
        print("1. Зашифровать сообщение / Encrypt a message")
        print("2. Расшифровать сообщение / Decrypt a message")
        print("3. Зашифровать заранее заданное сообщение / Encrypt a predefined message")
        print("4. Показать историю / Show history")
        print("5. Сохранить историю в текстовый файл / Save history to text file")
        print("6. Экспортировать историю в CSV / Export history to CSV")
        print("7. Очистить историю / Clear history")
        print("8. Выход / Exit")
        
        choice = input("Выберите опцию (select an option) 1–8: ").strip()
        # asks user to make selection from menu 1-8 
        # .strip removes white space 
        # user selection is stored in variable choice 
        
        if choice == "1": 
        # if 1 then program performs encryption on text that user inputs 
            user_message = input("Ввод текста: (input text) ")
            
            while True: 
            # will ask user for a valid shift number for encypting 
            # will only break once a valid number is recieved 
            
                shift_by = input("Введите номер смены: (enter shift number) ")
                # asking user to input a number 
                # where number user input is stored 
               
                try: 
                # used for error catching 
                # will try to convert input into an interger 
                # if sucessful it will break 
                # if failed moves to exception block for error handling 
                     
                    shift = int(shift_by)
                    # converting input to interger
                    
                    break
                    # if successful then break out of try block and continue with program 
                    
                except ValueError:
                # failed converstion to integer then ValueError is raised 
                
                    print("Пожалуйста введите допустимое число, Please Enter A Valid Number")
                    # printing correction message to the user to try again 
                    # will keep looping until the user gets it right 
            
            while True:
            # second loop asking the user if they want to keep case sensitivity or not
            # will continue until user gives a valid input 
            
                try:
                    case_selection = input("сохранить футляр, да/нет: (save the case, yes/no): ").strip().lower()
                    # asks user to input yes or no (english or russian)
                    # .strip() removes white space before and after input 
                    # .lower() puts all input in lowercase for comparison of valid responses  
                    
                    if case_selection in ("да", "yes", "y"):
                        case_sensitive = True
                        break
                        # user does wnat to preserve case sensitivty of original message
                        # exit the loop and proceed  
                        
                    elif case_selection in ("нет", "no", "n"):
                        case_sensitive = False
                        break
                        # user does not want to preserve case sensitivity of original message 
                        # exit loop and proceed 
                        
                    else:
                        raise ValueError("Неверный ответ, Invalid response")
                        # if no input matches valid options ValueError is raised 
                        # moving to the exception block instead of crashing out 
                        
                except ValueError:
                # catching the error from else block 
                
                    print("Пожалуйста, введите 'да', 'нет', 'yes', 'no', 'y' или 'n'")
                    print("Please enter 'yes', 'no', 'да', 'нет', 'y' or 'n'")
                    # printing for the user what happened 
                    # lets the keep trying until they figure out the correct input 
            
            user_cipher = Cipher.Cipher(shift = shift, case_sensitive = case_sensitive)
            # creating another instance of the Cipher class based on user input 
            # takes 2 arguments shift and case_sensitive 
            # stored in user_cipher 

            user_encrypted = user_cipher.encrypt(user_message)
            # calls the encrypt() method to use on user_cipher object 
            # passing user_message 
            # storing in user_encrypted 

            user_decrypted = user_cipher.decrypt(user_encrypted)
            # calling decrypt method on user_cipher object 
            # passes encrypted message 
            # stores decrypted message in user_decrypted 

            print("\nОригинал: (original)", user_message)
            print("Зашифрованный: (encrypted)", user_encrypted)
            print("Расшифрованный: (decrypted)", user_decrypted)
            print()

            print("*** История операций (History Ops Log) ***\n")
            
            user_cipher.show_history()
            # calling the show_history method from cipher class for this object 
            # will show all operations performed on user_cipher object/instance
            # lets the user track what they just did in the program 

        elif choice == "2":
        # if option 2 is selcted by the user decryption is performed 
        
            encrypted_message = input("Введите зашифрованное сообщение: (enter encrypted message) ")
            # user must enter a message that is already encrypted 
            # user could encrypt a message and then select this option to decrypt afterwards 
            # stored in encrypted_message variable 
            
            decrypted = cipher.decrypt(encrypted_message)
            # uses the decrypt() method from the cipher class 
            # taking encrypted_message and returning original back to user 
            # stored in variable decyrpted 
            
            print("Расшифрованный: (decrypted)", decrypted)

        elif choice == "3":
        # checking if option 3 then encrytping and decrypting predefined messages 
        # these messages are already stored in the program 
        
            message, translation = preset_messages_pairs[0]
            # retrieving first message pair stored in list preset_message_pairs
            # unpacking the tuple into variables 
            # message gets Russian text
            # translation English 
            
            print("Оригинальный текст на русском языке: ", message)
            # printing original Russian Text for user 
            
            print("English Translation of Original Text: ", translation)
            # printing english translation of original text for user 
            
            print()

            encrypted = cipher.encrypt(message)
            # encrypts russian message using encryt() method from cipher class 
            # storing result in encrypted variable
            # will use default cipher settings 
            # shift = 5, case_senstivie = True
            
            print("зашифрованный: (encrypted)", encrypted)
            print("\n")
            # prints encrypted version 

            decrypted = cipher.decrypt(encrypted)
            # decrpyting message back to original form using decrypt() from cipher class 
            
            print("расшифрованный: (decrypted)", decrypted)
            print("\n")
            # printing decrypted message for user 

            print("*** журнал истории ***\n")
            cipher.show_history()
            print("\n")
            # calling show_history() method from Cipher class 
            # will show list of all encryption and decryption on this cipher object 

        elif choice == "4":
        # checks if option 4 was selected by the user 
        # option 4 is show history 
        
            cipher.show_history()
            # calls the show_history() method from Cipher class 
            # will show log of all operations performed on this cipher object 
            # record of activity 

        elif choice == "5":
        # if option 5 then saving cipher history to a txt file 
        
            filename = input("Введите имя файла (или нажмите Enter для стандартного): ").strip()
            # asks user to enter a file name 
            # .strip() removes all leading and trailing white spaces in the input 
            # user can also hit enter for a default file name to be applied 
            # result stored in filename variable 
            
            cipher.save_history(filename if filename else "cipher_history.txt")
            # saving cipher history to a txt file 
            # calling the save_history() method from the Cipher class 
            # filename is based on either user input or default cipher_history.txt
            # filename if filename else means use what the user inputted for a file name 
            # else if empty (user hit enter) then use default listed 

        elif choice == "6":
        # if user selected 6 then exporting to csv file 
        
            filename = input("Введите имя CSV файла (или нажмите Enter для стандартного): ").strip()
            # asks user to enter a file name 
            # .strip() removes all leading and trailing white spaces in the input 
            # user can also hit enter for a default file name to be applied 
            # result stored in filename variable
            
            cipher.export_to_csv(filename if filename else "cipher_history.csv")
            # saving cipher history to a csv file
            # calling the export_to_csv() method from the Cipher class 
            # saves the history in a structured format defined in Cipher class
            # filename if filename else means use what the user inputted for a file name 
            # else if empty (user hit enter) then use default cipher_history.csv
            
      
        elif choice == "7":
            # if user selects 7 then clearing all cipher object history 
            confirm = input("Вы уверены? да/нет, Are You Sure? yes/no: ").strip().lower()
            # asks the user if they are sure they want to clear the history 

            if confirm in ("да", "yes", "y"):
                # if confirmed then clear 
                # if they put no or anything else this will be skipped and nothing will be cleared 
                cipher.clear_history()
                # clear_history method is called from cipher class 
               
                print("История очищена, History cleared.")
                # confirmation message 
                
            else:
                print("История сохранена, History preserved.")
                # if user changed their mind confirmation nothing deleted 
        

        elif choice == "8":
            print("До свидания! / Goodbye!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите число от 1 до 8")
            print("Wrong Choice. Please Select A Number 1-8")

# -----------------------------------------------------
#   ***** Run the Program *****
# -----------------------------------------------------

if __name__ == "__main__":
    main()
    
    # used to find out if the file is being run directly by the user 
    # __name__ is built in python variable 
    # if file is run directly (using .py) __name__ becomes __main__ 
    # when imported from another then __name__ takes name of import file 
    
    # == "__main__" is checking if __name__ is equal to __main__
    # if it is equal then directly running and use code in block 
    # if imported this block does not execute





