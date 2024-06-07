class Employee:
    num_of_employees = 0

    def __init__(self, name: str, emp_id: str):
        self.name = name
        self.emp_id = emp_id
        Employee.num_of_employees += 1

    @classmethod
    def get_num_employees(cls) -> int:
        return cls.num_of_employees

    @staticmethod
    def validate_emp_id(emp_id: str) -> bool:
        return emp_id.isdigit()

emp1 = Employee("John", "123456")
emp2 = Employee("Jack", "159456")
emp3 = Employee("James", "654321")

print(f"Total employees: {Employee.get_num_employees()}") 

valid_id = "9876568954"
invalid_id = "abc123bdf"
print(f"Is {valid_id} a valid employee ID? {Employee.validate_emp_id(valid_id)}")  
print(f"Is {invalid_id} a valid employee ID? {Employee.validate_emp_id(invalid_id)}")