import re

log_entries = """
[2023-04-15 10:31:12] INFO: User 'michael chan' logged in successfully with password 'passw0rd!'.
[2023-04-15 10:31:45] ERROR: Failed login attempt for user 'emma watson' with password 'qwerty123'.
[2023-04-15 10:32:03] INFO: User 'david lee' logged in successfully with password 'helloWorld2023'.
[2023-04-15 10:32:25] ERROR: Failed login attempt for user 'sarah connor' with password 'terminator'.
[2023-04-15 10:32:47] INFO: User 'lucas brown' logged in successfully with password 'g@me0n'.
[2023-04-15 10:33:05] ERROR: Failed login attempt for user 'nina dobrev' with password 'dr@cul@2020'.
"""

# '(.*)', ([^']*)
pattern = r"ERROR: Failed login attempt for user '([^']*)'"

list_of_users_failed_login = re.findall(pattern, log_entries)
print(list_of_users_failed_login)