from models import Employee,Position,Department,session


#add employee
def add_employee(first_name,last_name,email,department,position):
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

add_department("marketing","Responsible for marketing")