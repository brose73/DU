"""
Author: Brandon Rose
Date: 03-09-18
Class: ICT 4370
Assignment#: 9
Description: Django password validator makes sure passwords have a minimum length, at least one uppercase
letter, one lowercase letter, and a digit.
"""

from django.core.exceptions import ValidationError

def validate_pass(password):

    min_length = 8

    # At least MIN_LENGTH long
    if len(password) < min_length:
        raise ValidationError("The new password must be at least %d characters long." % min_length)

    # At least one uppercase letter
    if not any(c.isupper() for c in password):
        raise ValidationError("The new password must contain at least one upper case letter")

    # At least one lowercase letter
    if not any(c.islower() for c in password):
        raise ValidationError("The new password must contain at least one lower case letter")
   
    # At least one number
    if not any(c.isdigit() for c in password):
        raise ValidationError("The new password must contain at least one digit")
