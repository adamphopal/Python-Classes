#Context Managers - Efficiently Managing Resources
#Context Managers are great for when we need to setup or teardown some resources during use.
# So these can be used for: open and closing files, opening and closing database connections, etc
# we have a class version and a function version with a decorator of the same code with our context manager for opening, and writing into a file

#Custom Context manager class version with filename, and mode as init instance methods,
#enter method will open a file, and return the file(object we are working within context manager
#exit method will close the file
from contextlib import contextmanager

class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


#with statement runs within our enter method, and gets the return value
#
#with Open_File('sample.txt', 'w') as f:
#    f.write('Testing class custom context manager!')

#print(f.closed)

#using a function for the same code above
#function version with a decorator
#### Using contextlib ####
#generator function

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    yield f
    f.close()


with open_file('sample2.txt', 'w') as f:
    f.write('Testing fucntion version with a decorator')

print(f.closed)

