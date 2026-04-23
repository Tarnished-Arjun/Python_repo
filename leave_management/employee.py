from util import validate_leave

class Employee:
    def __init__(self, emp_id, name, department, leave_balance=11):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.__leave_balance = leave_balance   

    def apply_leave(self, days):
        if validate_leave(days):
            if days <= self.__leave_balance:
                self.__leave_balance -= days
                return f"{self.name} applied for {days} days leave."
            else:
                return "Insufficient leave balance!"
        return "Invalid leave request!"

    def get_leave_balance(self):
        return self.__leave_balance

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Dept: {self.department}, Balance: {self.__leave_balance}"