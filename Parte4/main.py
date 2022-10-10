#!/usr/bin/env python3
import sys
import random
import string
import colorama
import time

def main(): 
    if sys.argv[1] == "-mv":
        print("max value mode")
        mvmode(sys.argv[2])
    elif sys.argv[1] == "-utm":
        print("time mode")  
    else:
        print("Invalid input")  

def mvmode(max_number):

    for i in range(0,int(max_number)):
        n = random.choice(string.ascii_letters)
        print(n)
        input_char = input()
        
        if n == input_char :
            print("You typed letter "+ colorama.Fore.GREEN + input_char+colorama.Style.RESET_ALL)
        else :
            print("You typed letter "+ colorama.Fore.RED + input_char+colorama.Style.RESET_ALL)

def utmode(max_time):
    time
    for i in range(0,int(max_time))



if __name__ == "__main__":
    main()