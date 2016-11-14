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
