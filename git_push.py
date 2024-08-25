import subprocess
import sys

# the subprocess module in python runs commands automatically in the terminal
# the run function in the subprocess module executes in place, taking in a list as argument
# it then passes the items in that list, in the command line
# use a dunder operation to execute the function to ensure that the commit message input
# only runs if the file is run locally as a main file, and not imported as a module
# if its to be imported as a module, the commit message input wont run, instead, you make the function return
# values instead of printing directly to terminal
# this gives you the flexibility of doing something with the returned value


def github_push(commit_message):
    try:
        # call subprocess.run to automate adding changes
        subprocess.run(["git", "add", "."])

        # call subprocess.run to commit changes
        subprocess.run(["git", "commit", "-m", commit_message])

        # callsubprocess.run to automate git push
        subprocess.run(["git", "push"])

        print("Changes pushed successfully")

    except Exception as error:
        print(f"Error has occured: {error}")

    # run commit message only if the python file is run locally
    # dont, if the program is being imported as a module into another project file
if __name__ == "__main__":
    commit_message = sys.argv[1]

    # call function, passing in the commit message
    github_push(commit_message)
