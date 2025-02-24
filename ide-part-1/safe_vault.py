CORRECT_PASSWORD = "topS3cret"

"""
This is a multiline
block
comment, I can type
as many lines as I need to
"""
password = input("Enter the Password for the Safe: ")

# this is a single line comment
if password == CORRECT_PASSWORD:
    print("Welcome admin")
else:
    print("Incorrect username or password")