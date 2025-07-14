from pydantic import BaseModel, field_validator , ValidationError 
from datetime import datetime

class Employee(BaseModel):
    name: str
    employee_id: str
    department: str
    salary: float

    @field_validator("salary")
    def salary_must_be_positive(cls , v):
        if v <= 0:
            raise ValueError("Salary must be positive")
        return v
    
    def __str__(self):
        return f"{self.employee_id} - {self.name} - {self.department} - {self.salary:.2f}"
    
class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, employee_id, department, salary):
        if employee_id in self.employees:
            raise ValueError("ID already exists")
        if not name or not department:
            raise ValueError("Name and Department cannot be empty")
        employee = Employee(name=name, employee_id= employee_id, department= department, salary= salary)

        self.employees[employee_id] = employee
        return f"Added: {name}"
    
    def remove_employee(self, employee_id):
        if employee_id not in self.employees:
            raise ValueError("ID not found")
        name = self.employees[employee_id].name
        del self.employees[employee_id]
        return f"Removed: {name}"

    def update_salary(self, employee_id, new_salary):
        if employee_id not in self.employees:
            raise ValueError("ID not found")
        employee = self.employees[employee_id].model_copy(update={"salary": new_salary})
        self.employees[employee_id] = employee
        return f"Updated salary for {employee_id} to ${new_salary:.2f}"

    def find_by_department(self, department):
        return [emp for emp in self.employees.values() if emp.department.lower() == department.lower()]

    def calculate_average_salary_by_department(self, department):
        employees = self.find_by_department(department)
        if not employees:
            raise ValueError("No employees in department")
        return sum(emp.salary for emp in employees) / len(employees)

    def generate_report(self):
        sorted_employees = sorted(self.employees.values(), key=lambda x: x.salary, reverse=True)
        report = "Employee Report:\n"
        for emp in sorted_employees:
            report += str(emp) + "\n"
        report += f"Total: {len(sorted_employees)} employees"
        return report


# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()
    
    try:
        manager.add_employee("Alice", "E001", "HR", 50000)
        manager.add_employee("Bob", "E002", "IT", 60000)
        manager.add_employee("Charlie", "E003", "HR", 55000)
        manager.add_employee("David", "E004", "IT", 65000)

        print(manager.generate_report())

        print("\nIT Employees:")
        for emp in manager.find_by_department("IT"):
            print(emp)

        print(f"\nHR Average Salary: ${manager.calculate_average_salary_by_department('HR'):.2f}")

        print(manager.update_salary("E002", 62000))
        print(manager.remove_employee("E003"))

        print("\nUpdated Report:")
        print(manager.generate_report())

    except ValueError as e:
        print(f"Error: {e}")