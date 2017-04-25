'''Iteration is everywhere in Python itself, and generator functions
are an easy way for you to mimic their behavior. In this lab, you'll
re-invent some Python built-ins using generator functions.

Reference, if needed:
https://docs.python.org/3/library/functions.html

First, make your own version of the built-in range() function.
(Do not use range() to implement it. That's cheating!)

>>> r1 = myrange(3)
>>> type(r1)
<type 'generator'>
>>> for num in r1: print(num)
0
1
2

>>> r2 = myrange(1, 4)
>>> type(r2)
<type 'generator'>
>>> for num in r2: print(num)
1
2
3

>>> r3 = myrange(1, 6, 2)
>>> type(r3)
<type 'generator'>
>>> for num in r3: print(num)
1
3
5


Next, make your own version of enumerate.
(No cheating!)

>>> pets = ["goat", "frog", "turtle"]
>>> enum1 = myenumerate(pets)
>>> type(enum1)
<type 'generator'>
>>> next(enum1)
(0, 'goat')
>>> next(enum1)
(1, 'frog')
>>> next(enum1)
(2, 'turtle')
>>> next(enum1)
Traceback (most recent call last):
...
StopIteration

>>> enum2 = myenumerate(pets, 1)
>>> type(enum2)
<type 'generator'>
>>> next(enum2)
(1, 'goat')
>>> next(enum2)
(2, 'frog')
>>> next(enum2)
(3, 'turtle')
>>> next(enum2)
Traceback (most recent call last):
...
StopIteration


The built-in map() takes a function object, and a sequence, applying
that function to every item. Re-create it as mymap().

>>> def uppercase(s):
...     return s.upper()
...
>>> def triple(num):
...     return 3 * num
...
>>> upper_pets = mymap(uppercase, pets)
>>> type(upper_pets)
<type 'generator'>
>>> next(upper_pets)
'GOAT'
>>> next(upper_pets)
'FROG'
>>> next(upper_pets)
'TURTLE'
>>> next(upper_pets)
Traceback (most recent call last):
...
StopIteration

>>> tripled = mymap(triple, [2, 4, 6, 8])
>>> next(tripled)
6
>>> next(tripled)
12
>>> next(tripled)
18
>>> next(tripled)
24
>>> next(tripled)
Traceback (most recent call last):
...
StopIteration


The built-in zip() function joins two sequences. Make your own version.

>>> colors = ["purple", "orange", "silver"]
>>> instruments = ["trumpet", "guitar", "drum"]
>>> pairs = myzip(colors, instruments)
>>> type(pairs)
<type 'generator'>
>>> next(pairs)
('purple', 'trumpet')
>>> next(pairs)
('orange', 'guitar')
>>> next(pairs)
('silver', 'drum')
>>> next(pairs)
Traceback (most recent call last):
...
StopIteration

Like zip(), myzip() will stop when the shortest sequence ends.

>>> vehicles = ["truck", "motorcycle", "hovercraft", "van"]
>>> for color, vehicle in myzip(colors, vehicles):
...     print(color + " " + vehicle)
purple truck
orange motorcycle
silver hovercraft

Can you make myzip() work with generator objects too?  (Hint: Python
has a built-in function called iter(), which creates an iterator from
any sequence or generator object.)

>>> firstrange = myrange(4)
>>> secondrange = myrange(10, 26, 5)
>>> pairs = myzip(firstrange, secondrange)
>>> type(pairs)
<type 'generator'>
>>> next(pairs)
(0, 10)
>>> next(pairs)
(1, 15)
>>> next(pairs)
(2, 20)
>>> next(pairs)
(3, 25)
>>> next(pairs)
Traceback (most recent call last):
...
StopIteration

'''

# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.
