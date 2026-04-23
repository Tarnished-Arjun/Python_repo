from employee import Employee

class Manager(Employee):

    def approve_leave(self, request):
        request.status = "Approved"
        return f"Leave approved for {request.employee.name}"

    def reject_leave(self, request):
        request.status = "Rejected"
        request.employee._Employee__leave_balance += request.days
        return f"Leave rejected for {request.employee.name}"