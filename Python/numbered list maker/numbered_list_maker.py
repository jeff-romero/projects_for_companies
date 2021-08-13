# https://github.com/jeff-romero/

import sys

def print_numbered_list(length=10):
    for i in range(length):
        print(str(i + 1) + ". ")


def main():
    list_length = 10
    if (len(sys.argv) > 1):
        list_length = int(sys.argv[1])
    print_numbered_list(list_length)


main()
