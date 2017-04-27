'''

This is a quick typing exercise. You are to fill in the `max_by_key` function below.


>>> nums = ["12", "7", "30", "14", "3"]
>>> integers = [3, -2, 7, -1, -20]
>>> student_joe = {'gpa': 3.7, 'major': 'physics',
...                'name': 'Joe Smith'}
>>> student_jane = {'gpa': 3.8, 'major': 'chemistry',
...                 'name': 'Jane Jones'}
>>> student_zoe = {'gpa': 3.4, 'major': 'literature',
...                'name': 'Zoe Grimwald'}
>>> students = [student_joe, student_jane, student_zoe]


>>> max_by_key(nums, int)
'30'

>>> max_by_key(integers, abs)
-20


>>> best_gpa = max_by_key(students, get_gpa)
>>> best_gpa['name']
'Jane Jones'
>>> best_gpa['gpa']
3.8
>>> best_gpa['major']
'chemistry'


'''

def get_gpa(who):
    return who["gpa"]

# Copy in the code for max_by_key here:

def max_by_key(items, key):
    biggest = items[0]
    for item in items[1:]:
        if key(item) > key(biggest):
            biggest = item
    return biggest

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.
