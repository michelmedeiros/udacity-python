#Soma de dois numeros
def sum(a, b):
    a = a+ b
    return a
a =5
b = 2
print(sum(a,b))
print (a)
a = sum(a,b)
print(a)

#Quiz 1 - Calculo de um quadrado
def square(a):
    b = a*a
    return b
print(square(5))


# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

def abbaize(a, b) :
    s1 = a + b
    s2 = b + a
    return s1 + s2

print (abbaize('a','b'))
#>>> 'abba'

print (abbaize('dog','cat'))
#>>> 'dogcatcatdog'