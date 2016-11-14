"""Nested decorators.

We can chain 2 or more decorators to further modify function behavior
NOTE: The order of chaining matters
"""


def a_decorator(passed_in_function):
    """Decorator function."""
    def wrapper_function():
        print "Unpacking..."
        passed_in_function()
        print "Done! B-)"
    return wrapper_function


def another_decorator(passed_in_function):
    """Decorator function."""
    def wrapper():
        print "Initializing the awesome in..."
        for x in xrange(10, 0, -1):
            print x
        passed_in_function()
        print "Initialization completing..."
    return wrapper


@a_decorator
@another_decorator
def func():
    """A simple function that needs decoration."""
    print "==========================================> OK"

print func()
