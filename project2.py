# project2.py
# Epiphany Chua
# echua@csu.fullerton.edu
# CPSC 335 Project 2
# March 27 2022

"""
main file to execute the code using the files exhaustive.py and golden.py
"""
import exhaustive
import golden
import largestsum

def main():
    # PART 1 A
    # Runs the Exhaustive Fibonacci Algorithm and returns the 15th term
    print("Part 1A:")
    print(exhaustive.exhaustive_fib(15))

    print()
    # PART 1 B
    print("Part 1B:")
    # get user input for p and n
    p = golden.get_p()
    print("The input was", p)

    n = golden.get_n(p)
    print("The input was", n)

    # print the result of using equation 4 to get the nth term
    print("The {n}th term using equation 4 with p = {p}:".format(n = n, p = p))
    print(golden.formula4(n, p))

    # print the result of using equation 5 to get the nth term
    print("The {n}th term using equation 5:".format(n = n))
    print(golden.formula5(n))

    # Print the first 20 terms using equation 4
    print("The first 20 terms using equation 4 with p = n-1:")
    golden.print_formula4(20)

    # Print the first 20 terms using equation 5
    print("The first 20 terms using equation 5:")
    golden.print_formula5(20)

    # Print the first 20 terms using equation 4
    print("The first 20 terms using equation 4 with p = 1:")
    golden.print_formula4b(20, 1)

    # Check the maxim with F3 and F30
    golden.check_maxim(3,30)

    # PART 2
    print("Part 2:")
    largestsum.main()



if __name__ == "__main__":
    main()