class LeaveRequest:
    def __init__(self, employee, days):
        self.employee = employee
        self.days = days
        self.status = "Pending"

    def __str__(self):
        return f"{self.employee.name} requested {self.days} days leave - {self.status}"