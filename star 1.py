'''
#p1:
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird'''
#code
'''import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # Line 13 is usually the input reading line below
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")'''
#p2
'''problem statement
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Example


Print the following:

8
-2
15
Input Format

The first line contains the first integer, .
The second line contains the second integer, .

Constraints



Output Format

Print the three lines as explained above.

Sample Input 0

3
2
Sample Output 0

5
1
6'''
#code
'''if __name__ == '__main__':
    a = int(input())
    b = int(input())
    #first line add  two numbers
    sum = a+b
    print(sum)
    #diference of two numbers 
    diference = a-b
    print(diference)
    #product of two numbers 
    product = a*b 
    print(product)'''
#p3
'''The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

Example


The result of the integer division .
The result of the float division is .
Print:

0
0.6
Input Format

The first line contains the first integer, .
The second line contains the second integer, .

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333'''
#code
'''if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    
    print(a/b)
'''
#p4
'''The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16'''
#code
'''if __name__ == '__main__':
    n = int(input())
    for i in range (n):
        print(i**2)
'''
