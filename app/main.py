import sys


def main():
    # Uncomment this block to pass the first stage

    valid_commands = set()

    while True:
        sys.stdout.write("$ ")
        command = input()

        if command not in valid_commands :
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()
