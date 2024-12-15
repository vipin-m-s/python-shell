import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ \n")


    # Wait for user input
    command = input()

    if command == "invalid_command":
        sys.stdout.write(f"{command}: command not found")


if __name__ == "__main__":
    main()
