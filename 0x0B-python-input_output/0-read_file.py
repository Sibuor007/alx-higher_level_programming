#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout """

def read_file(filename=""):
    """
    func that reads a file (UTF8) and prints it to stdout
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
