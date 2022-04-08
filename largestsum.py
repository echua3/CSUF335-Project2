# largestsum.py
# Epiphany Chua
# echua@csu.fullerton.edu
# CPSC 335 Project 2
# Problem 2
# March 27 2022

"""
Part 2:	The	Largest	Sum Subarray Problem
The problem involves finding a contiguous part of an array of numbers that adds up to the	
maximum	possible sum.
input: a non-empty vector V of n integers
output: indices b, e such that 0 ≤ b < e ≤ n, such the slice V[b: e] has maximum sum
"""

def largestsum(V):
    """
    Find the contiguous part of an array of numbers that adds up to the	
    maximum	possible sum.
    input: 
    V a non-empty vector V of n integers
    output: 
    indices b, e such that 0 ≤ b < e ≤ n, such the slice V[b: e] has maximum sum
    """
    b = 0
    e = 1
    n = len(V)
    largesum = sum(V[b:e])
    for i in range(n):
        for j in range(i + 1, n + 1):
            currentsum = sum(V[i:j])
            # print(currentsum)
            if sum(V[i:j]) > largesum:
                b = i
                e = j
                largesum = currentsum
    return (b, e, largesum)

def main():
    # Sample inputs
    v1 = [10, 2, -5, 1, 9, 0, -4, 2, -2]
    b1, e1, _ = largestsum(v1)
    print("The largest sum subarray of {v1} is {v1sa}.".format(v1=v1, v1sa = v1[b1: e1]))

    v2 = [-7, 1, 8, 2, -3, 1]
    b2, e2, _ = largestsum(v2)
    print("The largest sum subarray of {v2} is {v2sa}.".format(v2=v2, v2sa = v2[b2: e2]))

    v3 = [9, 7, 2, 16, -22, 11]
    b3, e3, _ = largestsum(v3)
    print("The largest sum subarray of {v3} is {v3sa}.".format(v3=v3, v3sa = v3[b3: e3]))

    v4 = [6, 1, 9, -33, 7, 2, 9, 1, -3, 8, -2, 9, 12, -4]
    b4, e4, _ = largestsum(v4)
    print("The largest sum subarray of {v4} is {v4sa}.".format(v4=v4, v4sa = v4[b4: e4]))


if __name__ == "__main__":
    main()