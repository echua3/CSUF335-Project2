# golden.py
# Epiphany Chua
# echua@csu.fullerton.edu
# CPSC 335 Project 2
# Problem 1B
# March 27 2022

"""
B.	The	Golden Ratio Approach
a. Design algorithms to obtain the	Fibonacci numbers using	equations (4) and (5) above
When implementing equation (4), ask the	user to	enter 'p'. You should specify that ‘p’
should be a positive integer and non-floating point. If a wrong number is entered,	
inform	the	user and request for a new number, until a correct input is received. Then	
ask	the	user to	enter ‘n’. Use the calculated fp to obtain fn!.
When implementing equation (5), equation (3) should be used to find fn!
b. Print the first 20 terms of the sequence
c. Compareyour outputs when equation (4) is used against results from equation (5)
d. Check and confirm or disprove the maxim above using F3 and F30. (from equation	
5 implementation)
"""
import math

def formula3(n):
    """
    formula 3 function

    input
    n: integer, the nth value of the fibanacci sequence to calculate

    return
    Fn, the nth term of the fibanacci sequence calculated using the formula
    """
    return ((math.pow(1 + math.sqrt(5), n) - (math.pow(1 - math.sqrt(5), n))) / (math.pow(2, n) * math.sqrt(5)))


def formula4(n, p):
    """
    formula 4 function

    input
    n: positive integer nth value of the fibanacci sequence to calculate
    p: a postive integer less than n, the pth term in the sequence

    return
    Fn, the nth term of the fibanacci sequence calculated using the formula
    """

    fp = int(formula3(p))
    return float(fp * math.pow(((1 + math.sqrt(5)) / 2), n-p))



def formula5(n):
    """
    formula 5 function
    calculates the nth term of the fibinacci sequence by calulating the (n-1)
    term using formula 3, then multiplying by the golden ratio

    input
    n: positive integer nth value of the fibanacci sequence to calculate

    return
    Fn, the nth term of the fibanacci sequence calculated using the formula
    """

    fn = int(formula3(n-1))     # calculates the previous value in the sequence
    return float(fn * ((1 + math.sqrt(5)) / 2)) 

def print_formula4(n):
    """
    prints the first n numbers of the fibanacci sequence using formula 4

    input
    n: positive integer, the number of terms in the sequence

    return
    outputs the first n numbers 
    """
    i = 1
    while i <= n:
        if i == n:
            print(formula4(i, i-1))
        else:
            print(formula4(i, i-1), end = ', ')
        i = i + 1

def print_formula4b(n, p):
    """
    prints the first n numbers of the fibanacci sequence using formula 4

    input
    n: positive integer, the number of terms in the sequence
    p: a previous term in the sequence, must be less than n

    return
    outputs the first n numbers 
    """
    i = 1
    while i <= n:
        if i == p:
            print(formula4(i, i - 1), end = ', ')
        elif i == n:
            print(formula4(i, p))
        else:
            print(formula4(i, p), end = ', ')
        i = i + 1

def print_formula5(n):
    """
    prints the first n numbers of the fibanacci sequence using formula 5

    input
    n: positive integer, the number of terms in the sequence

    return
    outputs the first n numbers 
    """
    i = 1
    while i <= n:
        if i == n:
            print(formula5(i))
        else:
            print(formula5(i), end = ', ')
        i = i + 1

def get_p():
    """
    Obtain p from user input (positive integer and non-floating point)

    return
    p: (positive integer and non-floating point)
    """
    while True:
        try:
            p = int(input("Please enter p (non-floating point, postive interger): "))
        except ValueError:
            print("Enter a postive, non-floating point integer")
            # loop until correct value of p entered
            continue
        if p <= 0:
            print("p must be positive")
            continue
        else:
            break
    return p

def get_n(p):
    """
    Obtain n from user input (positive integer and non-floating point) that is greater than p
    input 
    p: non-floating point positive integer
    
    return
    n: (positive integer and non-floating point) greater than p
    """
    while True:
        try:
            n = int(input("Please enter n (non-floating point, postive interger) greater than p: "))
        except ValueError:
            print("Enter a postive, non-floating point integer")
            # loop until correct value of p entered
            continue
        if n <= 0:
            print("n must be positive")
            continue
        if n <= p:
            print("n must be greater than p")
        else:
            break
    return n

def check_maxim(a, b):
    """
    Checks maxim that the ratio of two consecutive Fibonacci numbers approaches the Golden	
    Ratio, as n gets bigger using equation 5
    input 
    a: small integer
    b: large integer
    
    return
    prints the results
    """
    # Print F3 using equation 5
    fa = formula5(a)
    print("F{a} = {fa}".format(a = a, fa = fa))
    fa1 = formula3(a - 1)
    print("F{a1} = {fa1}".format(a1 = a - 1, fa1 = fa1))

    # Print F30 using equation 5
    fb = formula5(b)
    print("F{b} = {fb}".format(b = b, fb = fb))
    fb1 = formula3(b - 1)
    print("F{b1} = {fb1}".format(b1 = b - 1, fb1 = fb1))

    # Print F(a):F(a-1) 
    rat1 = fa/fa1
    print("The ratio F{a}:F{a1} = {rat1}".format(a=a, a1 = a-1, rat1=rat1))


    # Print F(b):F(b-1)
    rat2 = float(fb/fb1)
    print("The ratio F{b}:F{b1} = {rat2}".format(b=b, b1 = b-1, rat2=rat2))

    # print the golden ratio
    golden = (1 + math.sqrt(5)) / 2
    print("Golden ratio = ", golden)

    # check the difference from the golden ratio
    print("|golden ratio - F{a}:F{a1}| = {abs1}".format(a=a, a1 = a-1, abs1 = abs(float(golden - rat1))))

    print("|golden ratio - F{b}:F{b1}| = {abs2}".format(b=b, b1 = b-1, abs2 = abs(float(golden - rat2))))

    
def main():
    # Obtain p from user input (positive integer and non-floating point)
    p = get_p()

    # Obtain n from user input (positive integer and non-floating point)
    n = get_n(p)

    print("p =", p, "n =", n)

    print("formula 3: Fn =", formula3(n))

    print("formula 4: Fn =", formula4(n, p))

    print("formula 5: Fn =", formula5(n))

    print()
    # B) 
    # print the first 20 terms of the sequence using equation (4)
    print("The first 20 terms using equation 4:")
    print_formula4(20)

    print()
    # print the first 20 terms of the sequence using equation (5)
    print("The first 20 terms using equation 5:")
    print_formula5(20)

    print()
    # There is a maxim	that the ratio of two consecutive Fibonacci numbers approaches the Golden	
    # Ratio, as n gets bigger
    # d. Check and confirm or disprove the maxim above using F3 and F30. (from equation	
    # 5 implementation
    check_maxim(3,30)


if __name__ == "__main__":
    main()
