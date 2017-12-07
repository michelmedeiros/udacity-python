
# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    count = 1
    fat = n
    if n == 0:
        fat = 1
    else:
        while n > count:
                fat = fat * (n - count)
                count = count + 1
    return fat

#n! = n . (n - 1)!  =  n . (n - 1) . (n - 2)!  =  n . (n - 1) . (n - 2) . (n - 3) . ... . 1!
#5 x 4 (20) X 3 (60)x 2 (120)X 1
print(factorial(0))

print(factorial(4))
#>>> 24
print (factorial(5))
#>>> 120
print (factorial(6))
#>>> 720