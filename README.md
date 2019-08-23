# SafePass
Before generating password for anything, make sure the password is unique by searching it in tons of passwords stored by hackers in various Password Dictionaries availablr online. Also you can easily add Password Dictionaries from internet yourself, it is as easy as copy and pasting the file. Be safe from Bruteforce Attacks, and choose a safe password by first verifying it.

## Installation and Running

Make sure you have python and pip installed, To check python and pip installation, run `python --version` and `pip --version` command in your terminal. 

Then Do: 
```git clone https://github.com/shivamsn97/SafePass
cd SafePass
pip3 install -r requirements.txt
python3 safe.py
```
## For Android
On android, download [Termux](https://play.google.com/store/apps/details?id=com.termux) app from Google Play.
Then once it is installed, open it and type following commands to install SafePass:

```
pkg install python
git clone https://github.com/shivamsn97/SafePass 
pip3 install SafePass/requirements.txt
```

Now to run SafePass, open termux and type these commands:

```cd SafePass
python3 safe.py
```

# To add new Password Dictionaries
Remember, Password Dictionary must be a text file with passwords seperated by NewLine Character.

To add a new such file, just copy paste it in the *PasswordDatas* folder in the SafePass directory.
Very soon, we will be adding a better implementation of importing new Password Dictionaries, but till then, this is the only way...