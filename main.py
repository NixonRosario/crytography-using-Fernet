# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from cryptography.fernet import Fernet # install cryptography and import Fernet

key = Fernet.generate_key() # generates random keys

file = open('keys.txt', 'a+')
file.write("keys:- " + str(key) + "\n") # converting bytes to string and store it in a file
file.close()


def cipher():
    obj = Fernet(key)  # the generated key is stored in variable obj
    user = input('Enter the encrypted: ') .encode() # .encode() is used to convert string to bytes
    encrypted = obj.encrypt(user) # .encrypt() is used to encrypt the text
    file = open('keys.txt', 'a+')
    file.write("Value:- " + str(encrypted) + "\n") # encrypted text is stored 
    file.close()
    print('Encrypted data:- ', encrypted)

    n = input('If you want to decrypt select (y/n):- ') # if y is enterd decryption will take place

    if n == 'y':
        decrypted = obj.decrypt(encrypted)
        utf = decrypted.decode('utf-8') # .decode() is used to convert bytes to text
        print("Decrypted msg:- ", utf)
    else:
        print("Thank You!!")


def all_files():
    obj = Fernet(key)

    file = open('key.txt', 'a+')
    file.write("KEYS:- " + str(key) + "\n") # key generated gets stored
    file.close()

    path = input('Enter the path for encryption- ') # path of the file is given
    print("Path of the file", path)
    img = open(path, "rb")
    img1 = img.read() # reads the file which is in the path
    img.close()

    encrypted = obj.encrypt(img1) # encrypts the image

    en = open(path, 'wb')
    en.write(encrypted) # returns the encryped file while opening the file
    en.close()

    print("Encrypted!!")
    
    n = input('Do you want to decrypt (y/n):- ')
    
    if n == 'y':
        en_file = open(path, "rb") 
        encrypted = en_file.read()  # reads the encrypted file
        en_file.close()

        decrypted = obj.decrypt(encrypted) # decrypts the encrypted file

        de = open(path, 'wb')
        de.write(decrypted) # returns the actual file
        de.close()
        print("Decrypted!!")

    else:
        print("Thank you!!")


cipher() # fuction call is made
all_files()
