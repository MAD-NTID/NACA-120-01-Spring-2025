import my_regex

my_regex.search(r'\d', "abc1234")
my_regex.search(r'\d+', "abc1234")

my_regex.match("Hello", "Hello, Welcome to my class")

my_regex.start_with("Welcome", "Welcome to RIT")
my_regex.start_with("Hello", "Welcome to RIT")

print("Is digit 'abc123'")
my_regex.is_digit("abc123")

print("Is digit '123'") 
my_regex.is_digit("123")

phone_numbers_list = [
    "+1-(123)-123-1234",
    "1-(123)-123-1234",
    "1-123-123-1234",
    "123-123-1234",
    "1231231234",
    "11231231234",
    "1(123)1231234",
    "+1(123)1231234"
]

for phone_number in phone_numbers_list:
    print(f"Is Valid Phone Number: {phone_number} - {my_regex.validate_phone_number(phone_number)}")

# phone_numbers_list = (
#     ("+1-(123)-123-1234"),
#     ("1-(123)-123-1234"),
#     ("1-123-123-1234"),
#     ("123-123-1234"),
#     ("1231231234"),
#     ("11231231234"),
#     ("1(123)1231234"),
#     ("+1(123)1231234")
# )

# print(f"Are all phone numbers valid: {my_regex.validate_phone_numbers(phone_numbers_list)}")

# Multie Line String
RITPhoneNumbers = """
RIT has many phone numbers, here are some numbers we use on campus:
123-123-1234
1-569-123-3654
+1-569-235-1245
1234567890
+11234567890
(123)-584-2369
4444
"""

my_regex.extract_phone_number(RITPhoneNumbers)

    