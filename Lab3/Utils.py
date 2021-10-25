import re

reserved_words_separators_operators = []

with open('tokens.in', 'r') as token_file:
    lines = token_file.readlines()
    for line in lines:
        reserved_words_separators_operators.append(line.strip('\n'))
token_file.close()


def check_if_number(text):
    if text == "0":
        return True
    regex = '^[+,-]?[1-9][0-9]*$'
    if re.search(regex, text):
        return True
    return False


def check_if_identifier(text):
    regex = '^[a-zA-Z][a-zA-Z_0-9]*$'
    if re.search(regex, text):
        return True
    return False


def check_if_string(text):
    regex = '^"[a-zA-Z0-9 ]+"$'
    if re.search(regex, text):
        return True
    return False


def check_if_constant(text):
    return check_if_string(text) or check_if_number(text)


def check_string_start_with_delimiter(text):
    for delimiter in reserved_words_separators_operators:
        if text.startswith(delimiter):
            return delimiter
    return False
