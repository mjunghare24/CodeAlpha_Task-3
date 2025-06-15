import re

# Open the input.txt file in the current directory
with open('input.txt', 'r') as file:
    text = file.read()

# Find all email addresses using regex
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

# Write the extracted emails to emails.txt
with open('emails.txt', 'w') as out_file:
    for email in emails:
        out_file.write(email + '\n')

print("✅ Extracted emails written to emails.txt.")
