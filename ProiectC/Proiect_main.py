import sys
from commom_phrases import *



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Not enough arguments")
    elif len(sys.argv) > 3:
        print("Too many arguments")
    elif  len(sys.argv) == 3:
        print(Show_common_phrases(sys.argv[1],sys.argv[2]))