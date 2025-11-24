import re
email_addresses = [
  "json.doe@example1.com",
  "jane.smith@example2.com",
  "foo@bar.com",
]

regex = re.compile(r"([^@]+)@(.+)")

for email in email_addresses:
    match = regex.match(email)
    if(match):
        username, domain = match.groups()
        print(f"username: {username}, Domain: {domain}")