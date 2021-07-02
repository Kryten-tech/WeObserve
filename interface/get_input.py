from .data import DATA
from .built_in_methods import input_

#returns the input provided by the users (converted to all-lowercase and stripped of whitespace)

def get_input():
    return input_(DATA["input_prompt"]).strip().lower()
