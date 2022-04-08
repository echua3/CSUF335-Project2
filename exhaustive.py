# exhaustive.py
# Epiphany Chua
# echua@csu.fullerton.edu
# CPSC 335 Project 2
# Problem 1A
# March 27 2022

"""
A.	The	Exhaustive Pattern
The	first approach will involve	recursive calculation of each member of the	sequence.	
a. Using the formular above, develop a recursive algorithm to calculate	the	nth terms of	
the	sequence. The first	term of	the	sequence is	0, as shown above.	
b. Print out the 15th term of the sequence.
"""


def exhaustive_fib(i):
    """
    exhaustive_alg function that uses recursion to calculate the nth member of the fibonnaci sequence

    input
    i: the number of terms

    returns
    the ith value of the fibonnacci sequence
    """
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return exhaustive_fib(i - 1) + exhaustive_fib(i - 2)

def main():
    # ask user for n
    # Obtain n from user input (positive integer and non-floating point)
    while True:
        try:
            n_terms = int(input("Please enter the number of terms in the Fibonacci sequence: "))
        except ValueError:
            print("Enter a non-negative, non-floating point integer")
            # loop until correct value of p entered
            continue
        if n_terms < 0:
            print("n must be non-negative")
            continue
        else:
            break
    i = n_terms

    nth_fib = exhaustive_fib(i)
    print("The {i}th term in the fibonacci sequence is {nth_fib}".format(i=i, nth_fib=nth_fib))

    # prints the 15th term of the sequence
    print("The 15h term is: ", exhaustive_fib(15))

if __name__ == "__main__":
    main()




