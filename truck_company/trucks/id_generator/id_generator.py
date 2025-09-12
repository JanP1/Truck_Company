import random
import string

def generate_identifier(length=7):
    """Generate a random uppercase alphanumeric string (default: 7 chars)."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
