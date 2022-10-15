from curses.ascii import isdigit
from http.client import SWITCHING_PROTOCOLS
from xmlrpc.client import boolean


def c():
    print("Enter the temperature to convert to C")


def f():
    print("Enter the temperature to convert to F")

def check(ans) :
    if (isdigit(ans)==True):
        if (ans == "1" or ans == "2"):
            return True;
        return False;
    return False;

print("Which conversion?\n [1] F to C ,OR\n [2] C to F");
ans = input(str(""));

if (check(ans)==True):
    if (ans == "1"):
        c();
    elif(ans == "2"):
        f();