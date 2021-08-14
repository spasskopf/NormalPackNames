import re
import sys
import os
import time
import random

searchExpression = r'^[! ]+'


def clean_directory(directory):
    if not os.path.isdir(directory):
        print(directory + " is not a directory! Skipping")
        return

    for file in os.listdir(directory):
        if re.search(searchExpression, file) is not None:
            name = re.sub(searchExpression, "", file)

            # Name only consists of filtered symbols
            if len(name) == 0:
                print(file + " only consists of filtered symbols! Using fallback name")
                name = "fallback_" + str(time.time_ns() + random.randint(0, 10000))

            if os.path.exists(directory + os.sep + name):
                print(file + " already exists! Appending current time")
                name += str(time.time_ns() - random.randint(0, 10000))

            os.rename(directory + os.sep + file, directory + os.sep + name)
            print("Renaming '" + file + "' -> '" + name + "'")


for arg in sys.argv:
    clean_directory(arg)
print("Finished")
