from .data import DATA
from .get_input import get_input
from .built_in_methods import print_

def get_boolean_input():
    while True:
        received_input = get_input()

        if received_input in DATA["forms_of_true"]:
            return True

        if received_input in DATA["forms_of_false"]:
            return False

        print_(DATA["unsuitable_input_messages"]["get_boolean_input"])
