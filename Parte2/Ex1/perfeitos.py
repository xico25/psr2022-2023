#!/usr/bin/env python3
# --------------------------------------------------
# A simple python script to print hello world!
# Francisco de Bastos Lopes.
# PSR, Setember 2020.
# --------------------------------------------------



def getDividers(number):

    dividers=[]

    for i in range(1,number):
        if number%i == 0:
            dividers.append(i)

    return dividers

def isPerfect(number):
    
    dividers = getDividers(number)

    if sum(dividers) == number:
        return True
    else: 
        return False



def main():
    maximum_number = 1000
    print("Testing for perfect numbers")
    for number in range(1, maximum_number+ 1):
        print("Analizing Number " + str(number))
        if isPerfect(number):
            print(str(number) + ' is perfect.')
        


if __name__ == "__main__":
    main()
  