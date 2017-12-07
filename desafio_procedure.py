# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.

def find_second(search, target):
    first_search = search.find(target)
    second_search = search.find(target, first_search + 1)
    return second_search

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print(find_second(danton, 'audace'))
#>>> 25

twister = "she sells seashells by the seashore"
print(find_second(twister,'she'))
#>>> 13


# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'

def is_friend(friend):
    if friend[0] == 'D':
        return True
    else:
        return False

print(is_friend('Diane'))
#>>> True

print(is_friend('Fred'))
#>>> False



# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(friend):
    if friend[0] == 'D' or friend[0] == 'N':
        return True
    else:
        return False

print (is_friend('Diane'))
#>>> True

print (is_friend('Ned'))
#>>> True

print (is_friend('Moe'))
#>>> False



# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.
def print_numbers(number):
    i = 0
    while i < number:
        i = i + 1
        print(i)

print_numbers(3)
# >>> 1
# >>> 2
# >>> 3



