from curses.ascii import isdigit
from http.client import SWITCHING_PROTOCOLS
from xmlrpc.client import boolean


def c():        #convert from F to C
    print("Enter the temperature to convert to C")


def f():       #convert from C to F
    print("Enter the temperature to convert to F")

def check(ans) :
    if (isdigit(ans)==True):
        return True;
    return False;


    

def main():

    while (True) :

        ans = input(str("Which conversion?\n [1] F to C ,OR\n [2] C to F"));
        typeEval = check(ans)

        if (typeEval == True) :
            if (ans == "1"):
                c();
            elif (ans == "2"):
                f();
            else :
                print("Huh?")
                continue;

        else :
            print("Could not get that")
            break;

    if (__name__ == "__main__"):
        main()
