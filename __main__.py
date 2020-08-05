from os import listdir
from os.path import isfile, join, dirname, realpath
from os import get_terminal_size
from sys import argv
from colorama import Fore, Back, Style 
from helper import hide_cursor, show_cursor, print_title, file_len, clear

data_path =  dirname(realpath(__file__)) + '/PasswordDatas'

files = [f for f in listdir(data_path) if isfile(join(data_path, f))]

def check_one ():
	clear ()
	#print ("in check 1")
	print_title ()
	strx = input (Fore.GREEN + "Enter the password you want to check: " + Fore.RED + "\n(It is CASE SENSITIVE and SPACES will also be counted)\n\n"+Fore.WHITE+"#" + Fore.BLUE + "")
	i = 0
	(Found, File) = (False, None)
	clear ()
	print_title ()
	print (Fore.GREEN + "\nSearching for " + Fore.RED + strx + Fore.GREEN + " in Password Database.\n")
	print(Fore.WHITE + "It may take Several Minutes. To interrupt, Press CTRL+C.\n\n")
	hide_cursor ()
	try:
		total_pass = 0
		for x in files:
			total_pass = total_pass + file_len (data_path + '/' + x)

		for x in files:
			if Found: 
				break
			file = open(data_path + '/' + x, 'r', encoding = 'latin1')
			(c, r) = get_terminal_size()
			print (Back.CYAN + (c-1)*' ', end = '\r')
				
			for line in file:
				line = line.strip ()
				#(c, r) = get_terminal_size()
				#print (Back.BLUE + (c-1)*' ', end = '\r')
				i = i+1
				zx = Back.CYAN + Fore.BLACK + "Checking " + Fore.MAGENTA + "{:>13}".format (line[:13]) + Fore.BLACK + " in file " + Fore.MAGENTA + "{:>25}  ".format ( x[:25] ) + Fore.RED + str((i*100)//total_pass) + "%"
				print (zx, end = '\r')
				if (line == strx):
					(Found,File) = (True, x)
					file.close ()
					break
			file.close ()
		(c, r) = get_terminal_size()
		print (Back.BLACK + (c-1)*' ', end = '\r')
		if Found:
			print (Fore.RED + "Your password was available in the password database in file " + Fore.BLUE + File + Fore.RED + ". You should immediately change this password if u have used it somewhere.")
		else:
			print (Fore.GREEN + "Great! Your password is not available in any of the Password Database, and it should be secure enough.")

		print (Fore.GREEN + "\n\n[+]" + Fore.WHITE + " Script Succeded. Result was " + Fore.BLUE + ("Unsecure Password" if Found else "Secure Password") + Fore.WHITE)
	except KeyboardInterrupt:
		(c, r) = get_terminal_size()
		print (Back.BLACK + (c-1)*' ', end = '\r')
		print (Fore.GREEN + "\n[+]" + Fore.WHITE + " Script Succeded. Result was " + Fore.BLUE + "Interrupted by User" + Fore.WHITE)
	show_cursor ()
	exit (0)

def check_file ():
	clear ()
	print_title ()
	print("This thing is under Development.")

def check_substr ():
	clear ()
	print_title ()
	strx = input (Fore.GREEN + "Enter the sub-string you want to search in Password Database: " + Fore.RED + "\n(It is CASE SENSITIVE and SPACES will also be counted)\n\n"+Fore.WHITE+"#" + Fore.BLUE + "")
	i = 0
	#(Found, File) = (False, None)
	clear ()
	print_title ()
	print (Fore.GREEN + "\nSearching for " + Fore.RED + strx + Fore.GREEN + " and its Sub-Strings in Password Database.\n")
	print(Fore.WHITE + "It may take Several Minutes. To interrupt, Press CTRL+C.\n\n")
	hide_cursor ()
	num = 0
	try:
		total_pass = 0
		for x in files:
			total_pass = total_pass + file_len (data_path + '/' + x)

		for x in files:
			file = open(data_path + '/' + x, 'r', encoding= 'latin1')
			(c, r) = get_terminal_size()
			print (Back.CYAN + (c-1)*' ', end = '\r')
				
			for line in file:
				line = line.strip ()
				#(c, r) = get_terminal_size()
				#print (Back.BLUE + (c-1)*' ', end = '\r')
				i = i+1
				zx = Back.CYAN + Fore.BLACK + "Checking " + Fore.MAGENTA + "{:>13}".format (line[:13]) + Fore.BLACK + " in file " + Fore.MAGENTA + "{:>25}  ".format ( x[:25] ) + Fore.RED + str((i*100)//total_pass) + "%"
				print (zx, end = '\r')
				l = line.find (strx)
				if (l is not -1):
					num = num + 1
					#l = line.find (strx)
					lenx = len (strx)
					linex = Fore.BLUE  + line[:l] + Fore.MAGENTA  + line [l:l+lenx] + Fore.BLUE  + line [lenx:]
					(c, r) = get_terminal_size()
					print (Back.BLACK + (c-1)*' ', end = '\r')
					print (Fore.WHITE  + "{:>6}: ".format (num) + " " + linex + " "  + Style.DIM + Fore.WHITE + " in " + Fore.BLUE  + x + Style.RESET_ALL)
					(c, r) = get_terminal_size()
					print (Back.CYAN + (c-1)*' ', end = '\r')
			file.close ()
		(c, r) = get_terminal_size()
		print (Back.BLACK + (c-1)*' ', end = '\r')
		
		print (Fore.GREEN + "\n\n[+]" + Fore.WHITE + " Script Succeded. Result was " + Fore.BLUE + "{} result(s)".format (num) + Fore.WHITE)
	except KeyboardInterrupt:
		(c, r) = get_terminal_size()
		print (Back.BLACK + (c-1)*' ', end = '\r')
		print (Fore.GREEN + "\n[+]" + Fore.WHITE + " Script Succeded. Result was " + Fore.BLUE + "Interrupted by User, {} results found.".format (num) + Fore.WHITE)
	show_cursor ()
	exit (0)

if len (files) is 0:
	print (Fore.RED + "[-]" + Fore.WHITE + " Empty Database. Please add some password lists in '{}/' directory...".format (data_path))
	show_cursor ()
	exit ()


print_title ()
print (Fore.GREEN + "\nCHOOSE YOUR SAFE-CHECK:\n")
print (Fore.BLUE + " 1. Check a Specific password in the database.\n 2. List Passwords containing a specified sub-string or word.\n 3. Check all Passwords present as list in a .txt file.\n\n\n")


while (True):
	x = input(Fore.GREEN + "ENTER YOUR CHOICE (0 to exit): "+ Fore.BLUE +"#")
	choice = 0
	try: 
		choice = int (x)
		if (choice > 3) or (choice < 0):
			raise Exception
		break
	except Exception as e:
		print (Fore.RED + "[-]" + Fore.WHITE + " YOU MISSED SOMETHING, PLEASE TRY AGAIN...")


if (choice == 0):
	#clear ()
	print (Fore.GREEN + "[+]" + Fore.WHITE + " Exiting. Hope you enjoyed")
	show_cursor ()
	exit()
	
try:
	if (choice == 1):
		check_one ()

	if (choice == 2):
		check_substr ()

	if (choice == 3):
		check_file ()
except Exception as e:
	#raise
	print (Back.BLACK + Fore.RED + "[-] " + Fore.WHITE + str (e))
	show_cursor ()
	exit (1)

show_cursor ()
print (Fore.GREEN + "[+]" + Fore.WHITE + " Exiting. Hope you enjoyed")
	