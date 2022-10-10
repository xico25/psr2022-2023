#!/usr/bin/env python3  


from curses import start_color
from time import time , ctime 

def tic():
    global starttime
    starttime = time()
    

def toc():
    print("Elapsed time is" + str(time()-starttime)+ "seconds()")


    

def main(): 
    tic()
    for i in range (0,50000001000):
     i**0.5
    toc()

if __name__ == "__main__":
    main()



