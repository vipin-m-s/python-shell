import sys


def main():
    # Uncomment this block to pass the first stage


    while True:
        sys.stdout.write("$ ")
        command = input()

        if ("invalid" in command) and ("command" in command) :
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()
