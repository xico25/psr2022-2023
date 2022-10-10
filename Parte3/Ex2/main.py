#!/usr/bin/env python3 



def addComplex(x, y):
     sr=x[0]+y[0]
     si=x[1]+y[1]
     st=[sr,si]
     return st


def multiplyComplex(x, y):
    mr=x[0]*y[0]-x[1]*y[1]
    mi=x[0]*y[1]+x[1]*y[0]
    mt=[mr,mi]
    return mt
     
def printComplex(x):
    r = x[0]
    i = x[1]
    print(str(r)+ '+' + str(i)+'i')
     
def main():
    # ex2 a)
    
    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)
    c3 = addComplex(c1, c2)
    printComplex(c3)
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()