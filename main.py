import argparse
import json
import os
import random
import re
import sys
import time
from zipfile import ZipFile

searchExpression = r'^[! ]+'


def log(string):
    if verbose:
        print(string)
    else:
        # Don't log if not verbose
        pass


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

            new_name = directory + os.sep + name
            old_name = directory + os.sep + file
            cleaned.append("%r -> %s" % (old_name, new_name))
            os.rename(old_name, new_name)
            log("Renaming '" + file + "' -> '" + name + "'")


def print_red(string):
    print("\033[91m {}\033[00m".format(string))


def print_green(string): print("\033[92m {}\033[00m".format(string))


def scan_directory(directory):
    for root, directories, files in os.walk(directory, topdown=True):
        for filename in files:
            fullname = os.path.join(root, filename)
            log(fullname)
            if filename.endswith(".zip"):
                with ZipFile(fullname, 'r') as zf:
                    if not zf.namelist().__contains__("pack.mcmeta"):
                        print_red("File " + fullname + " does not contain a pack.mcmeta File!")
                        invalid.append(f'{fullname} no pack.mcmeta')
                        continue
                    zf.read("pack.mcmeta")
                    with zf.open(name="pack.mcmeta", mode='r') as mcmeta:
                        try:
                            json.load(mcmeta)
                        except ValueError as error:
                            invalid.append(f"{fullname} invalid pack.mcmeta")
                            print_red(f"File {fullname} contains invalid pack.mcmeta!")
                            print(error)


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--search', action='store_true', dest='scan', help='Search for invalid Resourcepacks')
parser.add_argument('-c', '--clean', action='store_true', dest='clean', help='Clean Resourcepack names')
parser.add_argument('-v', '--verbose', action='store_true', help='Verbose Output')
parser.add_argument('directories', default=["."], nargs='*', type=str, help='Directories to perform action(s) on')
args = parser.parse_args()

if not args.clean and not args.scan:
    print("Either scan or clean are required!")
    print("Use --help for more details")
    sys.exit(1)

verbose = args.verbose
print('Scan: %r' % args.scan)
print('Clean: %r' % args.clean)
print('Verbose: %r' % verbose)

if args.clean:
    cleaned = []
    print("Cleaning resource pack names...")
    for d in args.directories:
        print("Directory: %r" % d)
        clean_directory(d)

if args.scan:
    invalid = []
    print("Scanning for invalid resource packs...")
    for d in args.directories:
        print("Directory: %r" % d)
        scan_directory(d)

if args.clean:
    print_green("==== SUMMARY ====")
    print_green(f"{len(cleaned)} cleaned files")
    for name in cleaned:
        print_red(name)
    print_green("=================")

if args.scan:
    print_green("==== SUMMARY ====")
    print_green(f"{len(invalid)} invalid files")
    for name in invalid:
        print_red(name)
    print_green("=================")


print("Finished")
