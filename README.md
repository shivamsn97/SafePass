# SafePass
Before generating password for anything, make sure the password is unique by searching it in tons of passwords stored by hackers in various Password Dictionaries availablr online. Also you can easily add Password Dictionaries from internet yourself, it is as easy as copy and pasting the file. Be safe from Bruteforce Attacks, and choose a safe password by first verifying it.

## Installation and Running

Make sure you have python and pip installed, To check python and pip installation, run `python --version` and `pip --version` command in your terminal. 

Then Do: 
```
git clone https://github.com/shivamsn97/SafePass
pip3 install -r SafePass/requirements.txt
python3 SafePass
```
## For Android
On android, download [Termux](https://play.google.com/store/apps/details?id=com.termux) app from Google Play.
Then once it is installed, open it and type following commands to install SafePass:

```
pkg install python git
git clone https://github.com/shivamsn97/SafePass 
pip3 install -r SafePass/requirements.txt
```

Now to run SafePass, open termux and type these commands:

```
python3 SafePass
```

# To add new Password Dictionaries
Remember, Password Dictionary must be a text file with passwords seperated by NewLine Character.

To add a new such file, just copy paste it in the *PasswordDatas* folder in the SafePass directory.
Very soon, we will be adding a better implementation of importing new Password Dictionaries, but till then, this is the only way...

Also, we have provided additional password Dictionaries available under the *PasswordDatas/Other Password Lists (Unused)* Directory, and you can copy paste them in the *PasswordDatas* directory to use them, but remember the bigger and more the Dictionaries are, the more time it takes to search.
