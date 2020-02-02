#!/usr/bin/python

import sys
import pyrebase
from getpass import getpass

config = {  "apiKey": "AIzaSyA25LKCxy0ruBc3c3-g5DzZkfyNQ64nxZQ",  "authDomain": "my-purchases-bb5f8.firebaseapp.com",  "databaseURL": "https://my-purchases-bb5f8.firebaseio.com",  "storageBucket": "my-purchases-bb5f8.appspot.com",  "serviceAccount": "my-purchases-bb5f8-firebase-adminsdk-e272n-daddec61f9.json" }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

username = ""
password = ""

for arg_num in range(len(sys.argv)):
    if ((sys.argv[arg_num]) == "-f"):
        receipt = open(sys.argv[arg_num + 1], "r")

        for line in receipt.read():
            pass

    if ((sys.argv[arg_num]) == "-u"):
        username = sys.argv[arg_num + 1]

    if ((sys.argv[arg_num]) == "-p"):
        password = sys.argv[arg_num + 1]

#authenticate a user
user = auth.sign_in_with_email_and_password(input("Username: "), getpass("authentication password: "))
