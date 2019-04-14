import time

def adder(a,b):
    for i in range(b):
        x = a + b * 10 / 7 + 2562 //11 * 357
    return x

# Takes a function and its arguments. Than it runs the function and returns the execution time
def timing(func, *args):
    start = time.time()             # Start timer
    func(*args)                     # Unpack args and pass them to the function, run function
    return time.time() - start      # Return total execution time.

def test(a, b):
    '''The function to pass'''
    print (a+b)

def looper(func, **kwargs):
    '''A basic iteration function'''
    for i in range(5):
        # Our passed function with passed parameters
        func(*tuple(value for _, value in kwargs.items()))

if __name__ == '__main__':
    # # This will print `3` five times
    # looper(test, a=1, b=2)

    print(timing(adder, 100, 200000))

