from interface import *
import observe

NGINX = "nginx"
TEST_DIRECTORY = "test_directory"
QUIT = "quit"

COMMANDS = [NGINX, TEST_DIRECTORY, QUIT]

def choose():
    while True:
        print_("Welcome to WeObserve.\n")
        print_("What would you like to monitor?: " + generate_readable_list(COMMANDS))
        command = get_command(COMMANDS)

        if command == NGINX:
            print(observe.observe())

        if command == TEST_DIRECTORY:
            print("oi")

        if command == QUIT:
            break


choose()
