"""A simple implementation of a decorator.

A decorator is simply a function that can wrap another functions
and modify their behavior.
Decorators let you execute code BEFORE and AFTER the FUNCTION they DECORATE
"""


def a_decorator(passed_in_function):
    """Decorator definition."""
    def do_something():
        print ("Doing something before executing passed in function")
        # Now call the passed in function
        passed_in_function()
        print ("Done executing the passed in function")

    # Notice we return a function without calling it
    # i.e do_something != do_something()
    return do_something


@a_decorator
def another_one():
    """A function that is wrapped by a decorator."""
    # Do some work here
    for x in xrange(1, 5):
        print ("I have mastered the art of decoration!")

print another_one()
# NOTE
# the use of @decorator_name is just a short way of saying:
another_one = a_decorator(another_one)
another_one()
