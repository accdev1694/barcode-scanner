import sys

# ensure user types in their name as second command line argument
def check_args(arguments):
    if len(arguments) == 2:
        return sys.argv[1]
    else:
        sys.exit("You must provide 2 command line arguments\n")