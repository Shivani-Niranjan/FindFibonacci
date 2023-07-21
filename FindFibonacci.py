'''
Given a number A, find and return the Ath Fibonacci Number using recursion.

Input 1:
A = 2

Input 2:
A = 9

Output 1:
1

Output 2:
34

'''

def fibonacci(n):
    if (n == 1) or (n==0):
        return n
    return fibonacci(n-1) + fibonacci(n-2)
 
 
if __name__ == "__main__":
    input = int(input())
    print(fibonacci(input))