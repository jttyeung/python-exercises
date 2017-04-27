# Find a way to have this function throw an error when run

def print_args(*args):
    for arg in args:
        print arg

# print_args(1, 2, 3)
print_args(-1,[print_args(2)])
key = 'hello'
print_args(key)

# errors out with keyword arguments
# print_args(a=0, b=1)
# use **kwards instead
