"""A stopwatch implementation."""
import time


def stopwatch(func):
    """Return the time taken to execute a given function."""
    def wrapper():
        start = time.time()
        func()
        stop = time.time()
        print "Time taken is: {: .2f}".format((stop - start) * 1000) + "ms"
    return wrapper


@stopwatch
def tester():
    """Do some work on lists."""
    results = []
    # Print a list in reverse
    for x in xrange(10000, 0, -1):
        results.append(x)
    print results

print tester()
