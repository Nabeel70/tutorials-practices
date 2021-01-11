def announce(f):
    def wrapper():
        print("About to run the function..")
        f()
        print("Done with the function")
    return wrapper

# Now using decorator
@announce
def hello():
    print("Hello and Welcome")
    
hello()