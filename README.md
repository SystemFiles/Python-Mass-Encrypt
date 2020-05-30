# Python Mass Encrypt
An open-source full filesystem encryption/decryption framework/payload

**WARNING** RUNNING THIS PROGRAM OUTSIDE OF A SANDBOX ENVIRONMENT COULD RESULT IN SEVERE DATA LOSS

*** I AM NOT RESPONSIBLE FOR ANYTHING YOU CHOOSE TO DO WITH THIS OPEN-SOURCE SOFTWARE ***

## About
Well technically this software could be described as ransomware, which is why I implore you not to use it on yours or anyone elses computer without permission and for educational purposes...

I made this project to learn how encryption/decryption libraries in python functioned and how attacks could potentially use these libraries to easily build ransomware that could be just as damaging as popular ransomware viruses out there right now...

**this was made for EDUCATIONAL PURPOSES ONLY**

~ Stay safe folks! and remember (DO NOT RUN THIS OUTSIDE OF SANDBOX ENV)

## Features
- Encrypts recursively from base directory
- Generates and emails a decryption key using gmail SMTP service
- SHA-256 with AES encryption
- Configurable descryption key at users discression
- Modular encrypt/decrypt so it can be implemented in custom payloads
- Decryption module allows full decryption of all (.enc) encrypted files using provided key (**note: danger**)
- Cryware2 provided as base payload to run attack and send email with key (**again for educational purposes**)

## Requirements
Python == 2.7.x
pycryptodome == 3.9.7

## How to run
If you do want to run this....you'll have to figure it out yourself (it's not that hard...) because I'm not going to just give the commands right here to potentially destroy data.

*Hint: generate payload with pyinstaller for best results...*

**note:** I have included a Dockerfile so you can test this in a containerized environment if you would like to see it run safely!

## Contact
Ben Sykes => bensykes12@gmail.com