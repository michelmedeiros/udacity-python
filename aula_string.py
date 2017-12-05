#QUIZ 1, 2
#Numbers
a, x = 1, 2
a = x
a = a + 1
print('Item 1')
print(x)

a, x = 1, 2
x = x + 1
x = x
print('Item 2')
print(x)

a, x = 1, 2
a, x = x, a
a, x = x, a
print('Item 3')
print(x)

a, x = 1, 2
z = x
a = z
x = a
print('Item 4')
print(x)

a, x = 1, 2
a = x
x = a
print('Item 5')
print(x)

#QUIZ 3 Strings
#Dada uma string s, qual dos abaixo sempre tem o mesmo valor que s? (Cuidado, s pode ser " ")
s = 'Michel'
s1 = ('a' + s)[1:]
print(s1)

s2 = s[0] + s[1:]
print(s[0]+s[1:])

s3 = s + ' '
print(s3)

s4 = s[0:]
print(s4)


#QUIZ 4 Strings
# Given the variables s and t defined as:
# write Python code that prints out udacious
# without using any quote characters in
# your code.
s = 'udacity'
t = 'bodacious'

print(s[0:4] + t[5:])

#QIUZ 5 String
# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo"
print(text.find('hoo'))

#QUIZ 6 Strings
# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip'
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped'
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are compress"
first = text.find('zip')
print(text.find('zip', first + 1))