import random

def validate_leave(days):
    return days > 0

def generate_employee_id():
    return random.randint(1000, 9999)