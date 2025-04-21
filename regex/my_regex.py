import re

def search(regex, data):
    # Run search
    match = re.search(regex, data)

    if(match is None):
        print("No match could be found")
    else:
        print(f"Match is found: {match.group()}")

def match(regex, data):
    # Run match
    match = re.match(regex, data)

    if match is None:
        print("Nothing was found")
    else:
        print(match.group())

def start_with(regex, data):
    regex = r'' + regex
    match = re.match(regex, data)

    if match is None:
        print(False)
    else:
        print(True)

def is_digit(data):
    # Digits Only
    regex = r'^\d+$'
    match = re.search(regex, data)

    if match is None:
        print(False)
    else:
        print(True)

def extract_phone_number(phone_number):
    regex = r'\+?\d?-?\(?\d{3}\)?-?\d{3}-?\d{4}'

    matches = re.findall(regex, phone_number)

    if matches is None:
        print("No Matches Found")
    else:
        print("Match Found")

def validate_phone_number(phone_number):
    regex = r'\+?\d?-?\(?\d{3}\)?-?\d{3}-?\d{4}'

    match = re.match(regex, phone_number)

    return match is not None

def validate_phone_numbers(phone_numbers):
    regex = r'\+?\d?-?\(?\d{3}\)?-?\d{3}-?\d{4}'

    matches = re.findall(regex, phone_numbers)

    if matches is not None:
        return len(matches) > 0
    
    return False