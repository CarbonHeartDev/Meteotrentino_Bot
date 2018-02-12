import os


def relative_to_absolute(relativa):
    return (os.getcwd() + relativa)
