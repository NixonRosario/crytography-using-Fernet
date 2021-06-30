# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from cryptography.fernet import Fernet

key = Fernet.generate_key()

file = open('keys.txt', 'a+')
file.write("keys:- " + str(key) + "\n")
file.close()


def cipher():
    obj = Fernet(key)
    user = input('Enter the encrypted: ') .encode()
    encrypted = obj.encrypt(user)
    file = open('keys.txt', 'a+')
    file.write("Value:- " + str(encrypted) + "\n")
    file.close()
    print('Encrypted data:- ', encrypted)

    n = input('If you want to decrypt select (y/n):- ')

    if n == 'y':
        decrypted = obj.decrypt(encrypted)
        utf = decrypted.decode('utf-8')
        print("Decrypted msg:- ", utf)
    else:
        print("Thank You!!")


def all_files():
    obj = Fernet(key)

    file = open('key.txt', 'a+')
    file.write("KEYS:- " + str(key) + "\n")
    file.close()

    path = input('Enter the path for encryption- ')
    print("Path of the file", path)
    img = open(path, "rb")
    img1 = img.read()
    img.close()

    encrypted = obj.encrypt(img1)

    en = open(path, 'wb')
    en.write(encrypted)
    en.close()

    print("Encrypted!!")
    n = input('Do you want to decrypt (y/n):- ')
    if n == 'y':
        en_file = open(path, "rb")
        encrypted = en_file.read()
        en_file.close()

        decrypted = obj.decrypt(encrypted)

        de = open(path, 'wb')
        de.write(decrypted)
        de.close()
        print("Decrypted!!")

    else:
        print("Thank you!!")


cipher()
all_files()
