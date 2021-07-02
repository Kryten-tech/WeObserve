def generate_readable_list(list_to_process):
    """
    Generate the message for get_command() to print when the user provides an
    input that does not match any commands.

    Examples
    --------
    >>> _generate_get_command_unsuitable_input_message(
    ...     ["nginx", "test_directory","logs"]
    ... )
    "You must enter \"nginx\", \"test_directory\", or \"logs\"."
    """
    # Put quotes around each string.
    processed_list = ["\"{}\"".format(item) for item in list_to_process]

    if len(processed_list) > 1:
        processed_list.append("or " + processed_list.pop())

    delimiter = " "

    if len(processed_list) > 2:
        delimiter = "," + delimiter

    return delimiter.join(processed_list)
