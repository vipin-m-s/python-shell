import sys


def main():
    # Uncomment this block to pass the first stage

    builtin_commands = {"exit", "echo", "type"}

    while True:
        sys.stdout.write("$ ")
        command = input()

        if command == "exit 0":
            sys.exit(0) 
        
        elif command.startswith("echo") :
            sys.stdout.write(command.split("echo ")[1])
        
        elif command.startswith("type"):
            command_to_check = command.split("type ")[1]

            if command_to_check in builtin_commands:
                sys.stdout.write(f"{command_to_check} is a shell builtin")
            else:
                sys.stdout.write(f"{command_to_check}: not found")
    
        else: 
            sys.stdout.write(f"{command}: command not found")

        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
