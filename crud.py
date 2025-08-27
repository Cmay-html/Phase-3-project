from models import Employee,Position,Department,session


#add employee
def add_employee(first_name,last_name,email,department_name,position_title):
    department = session.query(Department).filter(Department.name == department_name).first()
    position = session.query(Position).filter(Position.title == position_title).first()
    employee = Employee(
        first_name = first_name,
        last_name = last_name,
        email = email,
        department = department,
        position = position
    )
    session.add(employee)
    session.commit()

#add department
def add_department(name,description):
    department = Department(
        name = name,
        description = description
    )  
    session.add(department)
    session.commit()

#add position
def add_position(title,description):
    position = Position(
        title = title,
        description = description
    )  
    session.add(position)
    session.commit()


# Add department
def add_department(name, description):
    department = Department(
        name=name,
        description=description
    )
    session.add(department)
    session.commit()

# Add position
def add_position(title, description, department_name):
    department = session.query(Department).filter(Department.name == department_name).first()
    position = Position(
        title=title,
        description=description,
        department = department
    )
    session.add(position)
    session.commit()




# add_department("marketing","Responsible for marketing")

def view_all_departments():
    departments = session.query(Department).all()
    for department in departments:
        print(f"ID: {department.id}, Name: {department.name}, Description: {department.description}")


def view_all_positions():
    positions = session.query(Position).all()
    for position in positions:
        print(f"ID: {position.id}, Title: {position.title}, Description: {position.description}")

def view_all_employees():
    employees = session.query(Employee).all()
    for employee in employees:
        print(f"ID: {employee.id}, Name: {employee.first_name} {employee.last_name}, Email: {employee.email}")

def view_department_positions():
    positions = session.query(Position).all()
    for position in positions:
        print(f"ID: {position.id}, Title: {position.title}, Description: {position.description}")

def view_department_employees(depName):
    employees = session.query(Employee).filter(Employee.department.name == depName).all()
    for employee in employees:
        print(f"First Name: {employee.first_name}, Last Name: {employee.last_name}, Position: {employee.position.title}")


              