import sys

# ensure user types in their name and task as second and third command line arguments
def check_args(arguments):
    if len(arguments) == 3:
        user_name, task = arguments[1], arguments[2]
        return user_name, task
    else:
        sys.exit("You must provide 3 command line arguments\n")