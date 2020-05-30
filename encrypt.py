# Encrypt.py used to encrypt files
# Author: SystemFiles
# This file will handle the encryption of your files 
# AGAIN: DO NOT USE THIS IF YOU DONT WANT TO POTENTIALLY LOSE ALL YOUR FILES/CORRUPT YOUR PC!

import random, os
from Crypto.Hash import SHA256
from Crypto.Cipher import AES


def encrypt(key, filename):
    '''

    Encrypts given file 'filename' with AES encryption using a SHA256 key and appends the .enc extention to
    the encrypted file to identify them.

    :param key: The key used to generate the AES encryption for this file
    :param filename: The file being encrypted
    :return: Nothing
    '''

    chunk_size = 64*1024
    output_file = filename + ".enc"
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = ""

    for i in range(16):
        IV += chr(random.randint(0, 0xFF))

    # The AES-Encryptor!
    cryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, "rb") as in_file:
        with open(output_file, "wb") as out_file:
            out_file.write(file_size)
            out_file.write(IV)

            while True:
                chunk = in_file.read(chunk_size)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - (len(chunk) % 16))

                out_file.write(cryptor.encrypt(chunk))
    os.remove(filename)  # REMOVE ORIGINAL UNENCRYPTED FILE
    print("Original File Removed")


def decrypt(key, filename):
    '''

    Decrypts given file with extention .enc

    :param key: The key used to encrypt the data previously
    :param filename: The encrypted file
    :return: Nothing
    '''

    chunk_size = 64 * 1024
    output_file = filename[:-4]

    with open(filename, "rb") as in_file:
        file_size = long(in_file.read(16))
        IV = in_file.read(16)

        cipher = AES.new(key, AES.MODE_CBC, IV)

        with open(output_file, "wb") as out_file:
            while True:
                chunk = in_file.read(chunk_size)

                if len(chunk) == 0:
                    break;

                out_file.write(cipher.decrypt(chunk))
            out_file.truncate(file_size)


def get_key(password):
    '''

    Generates a SHA256 HASH for the given password and returns
    it as a key for encryption

    :param password: The password the user wants to use.
    :return: The SHA256 HASH key for encryption
    '''

    hasher = SHA256.new(password)
    return hasher.digest()
