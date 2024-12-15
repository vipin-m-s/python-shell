import sys


def main():
    # Uncomment this block to pass the first stage

    valid_commands = {"exit 0"}

    while True:
        sys.stdout.write("$ ")
        command = input()

        
        
        if command == "exit 0":
            sys.exit(0) 
        elif command.startswith("echo") :
            sys.stdout.write(command.split("echo ")[1])
        else: 
            sys.stdout.write(f"{command}: command not found")

        sys.stdout.write("\n")
        
if __name__ == "__main__":
    main()
