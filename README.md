#### Decorators demystified
Most python programmers fear decorators. They are simply functions that wrap other
functions and modify their behavior in the process.

For instance, if I want to run something before or/and after i execute my function,
I can employ the use of decorators to do just that!

Code reusability and abstraction are among the benefits you will get from using
decorators. Professional python programmers use decorators too. :-)

#### Requirements
For cloning, ensure you have installed Python 2.7+
No pip installs! Simple and easy. :-)

#### Quick Usage
You do not have to clone the repo. Just paste the code from decorators.py into a repl
and click run. Magic happen at [repl](repl.it)

#### Local
Run ``` python decorators.py ```

#### Explanation
In python, functions can be passed into other functions.
For example:

```
def func(pass_a_func):
    return pass_a_func()
```
Also, functions can wrap other functions.
```
def func():
    def wrapped_func():
       print "Long ago in a far distant land..."
    return wrapped_func
```

You can also return a function without calling it
```
def func(passed_in_func):
    def wrapped_function():
        print "Before the final blow was struck, I flung him into..."
        passed_in_func()
    # Return a function without calling it
    return wrapped_function

```
If you don't put parenthesis e.g wrapped_function(), a function can be passed around and can be assigned to other variables without executing it.
