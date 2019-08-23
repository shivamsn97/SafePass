import sys
import os
from colorama import Fore, Back

if os.name == 'nt':
    import msvcrt
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = False
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ci.visible = True
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

def print_title ():
	print (Back.BLACK)
	clear ()
	print (Fore.GREEN + "\n\n\nPASSWORD CHECK TOOL by SHIVAM")
	print (Fore.GREEN + "-----------------------------")
	print (Fore.RED + "check if your passwords are vurneuable by a bruteforce attack.\n\n\n")

def file_len(fname):
    with open(fname, encoding = 'latin1') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def clear ():
	if os.name == 'nt':
		os.system("cls")
	elif os.name == 'posix':
		os.system ("clear")