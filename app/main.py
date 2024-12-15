import sys


def main():
    # Uncomment this block to pass the first stage

    valid_commands = {"exit 0"}

    while True:
        sys.stdout.write("$ ")
        command = input()

        if command not in valid_commands :
            sys.stdout.write(f"{command}: command not found\n")
        
        if command == "exit 0":
            sys.exit(0) 

if __name__ == "__main__":
    main()
