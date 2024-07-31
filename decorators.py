'''
A decorator is a function that recieves a function as input and returns a modified version of that 
function or its output as a result.
'''

# Explicit Example of a decorator or wrapper function
def announce(f):
    def wrapper():
        print("About to run the function....")
        # Execute the function
        f()
        print("Done with the function")
        return wrapper
