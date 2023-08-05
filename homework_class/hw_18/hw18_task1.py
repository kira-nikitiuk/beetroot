# Create a class method named `validate`, 
# which should be called from the `__init__` method to validate parameter email, 
# passed to the constructor. The logic inside the `validate` method could be to check 
# if the passed email parameter is a valid email string.

import re

class EmailValidator:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        if not self.is_valid_email(self.email):
            raise ValueError("Invalid email format")

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

if __name__ == "__main__":
    try:
        valid_email = EmailValidator("kira@kira.com")
        print("Valid email:", valid_email.email)
        
        invalid_email = EmailValidator("invalid-email")
        print("Invalid email:", invalid_email.email)
    except ValueError as e:
        print("Error:", e)
