import re
import sys
import os

searchExpression = r'^[! ]+'


def clean_directory(directory):
    if not os.path.isdir(directory):
        print(directory + " is not a directory! Skipping")
        return

    for file in os.listdir(directory):
        if re.search(searchExpression, file) is not None:
            name = re.sub(searchExpression, "", file)
            os.rename(directory + os.sep + file, directory + os.sep + name)
            print("Cleaning '" + file + "' -> '" + name + "'")


for arg in sys.argv:
    clean_directory(arg)
