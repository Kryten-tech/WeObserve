from .data import DATA
from .built_in_methods import input_

def get_input():
    # Call input() with a predefined prompt and return the normalized result.
    return input_(DATA["input_prompt"]).strip().lower()
