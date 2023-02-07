#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

filename = "file_2"
text = "Holberton School is so cool!\n"
nb_characters_added = append_write(filename, text)
print(nb_characters_added)