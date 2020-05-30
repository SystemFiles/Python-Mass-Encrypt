# DECRYPTION PROGRAM
# Author: SystemFiles

# Run the program and enter a decryption key to unlock your files
# PLEASE NOTE: IF YOU ENTER AN INVALID KEY TO DECRYPT YOUR FILES 
# YOU WILL CORRUPT ALL OF THE ENCRYPTED FILES 
# (this is to be fixed later)....

import os
from encrypt import decrypt, get_key

HOME_DIR = os.path.expanduser("~")


def get_files(start_dir):
    '''
    Finds all the absolute files/paths for all files in start_dir recursively
    :param start_dir: The starting directory
    :return: Array containing all files
    '''
    result = []

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith('.enc'):
                result.append(os.path.join(root, file))
            else:
                print("File not encrypted...skipping")

    return result


if __name__ == '__main__':
    print("========= [ DECRYPTION PROGRAM ] =========="
            "\nNOTE: Incorrectly entered decryption key will result in PERMANENT loss of data. "
            "Only enter in the correct key.")
    password = raw_input("Enter the decryption key > ")

    for file in get_files(HOME_DIR):
        if file.endswith(".enc"):  # Check if file is encrypted at all
            decrypt(get_key(password), file)
            print("Decrypted {}".format(file))
        else:
            print("File not encrypted...skipping")
    choice = raw_input("Do you want to delete encrypted files? [Y/N] > ")
    if choice == "Y":
        for file in get_files(HOME_DIR):
            if file.endswith(".enc"):
                os.remove(file)
                print(file + " removed from system...")
        print("Done!")
    else:
        print("Encrypted files will remain on your machine..")
    print("All files have successfully been decrypted. Have a nice day!")