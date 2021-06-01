#goes into a given directory from the current path, and prints all files in that directory
#then goes back to the current path
import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

#we can reuse the context manager over and over again

with change_dir('/Users/samehphopal/classes'):
    print(os.listdir())


#with change_dir('/Users/samehphopal/NewPrac'):
#    print(os.listdir())

#with change_dir('/Users/samehphopal/desktop'):
#    print(os.listdir())

