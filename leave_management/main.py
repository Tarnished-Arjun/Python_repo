from employee import Employee
from manager import Manager
from leave import LeaveRequest
from util import generate_employee_id
from data import employees, leave_requests

emp1 = Employee(generate_employee_id(), "Arjun", "IT")
emp2 = Employee(generate_employee_id(), "Rossi", "HR")

mgr = Manager(generate_employee_id(), "Maager", "Admin")

employees.append(emp1)
employees.append(emp2)
employees.append(mgr)

req1 = LeaveRequest(emp1, 3)
print(emp1.apply_leave(3))
leave_requests.append(req1)

req2 = LeaveRequest(emp2, 5)
print(emp2.apply_leave(5))
leave_requests.append(req2)

print(mgr.approve_leave(req1))
print(mgr.reject_leave(req2))

print("\nLeave Requests:")
for req in leave_requests:
    print(req)

print("\nEmployee Details:")
for emp in employees:
    print(emp)