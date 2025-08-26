import click 
from datetime import datetime
from models import Department,Position,Employee,session
from crud import add_department,add_employee,add_position

def workplace():
    click.secho("Welcome To Workplace App", fg='blue', bg="white", bold=True)
    click.secho('Select an option to proceed', fg="yellow")
    click.secho('   1. Departments  \n   2. Positions  \n   3. Employees', fg='blue')

    choice = click.prompt("Select Option", type=int)

    if choice not in [1, 2, 3]:
        print("Invalid choice!Please select 1,2or 3 to proceed")
        return workplace()
    if choice == 1:
        while True:
            click.secho(".....DEPARTMENTS.....", fg = 'yellow')
            click.secho('   1. Add New Departments  \n   2. View All Departments  \n   3. View Department Employees  \n   4. View Department Positions', fg='blue')

            department_option = click.prompt("Select Department Option", type=int)

            if department_option in[1,2,3,4]:
                break
            else:
                print("Kindly enter a valid choice!")
                continue
        if department_option == 1:
            click.secho()


    if choice == 2:
        while True:
            click.secho(".....POSITIONS.....", fg = 'yellow')
            click.secho('   1. Add New Position  \n   2. View All Positions  ', fg='blue')

            position_option = click.prompt("Select Position Option", type=int)


    if choice == 3:
        while True:
            click.secho(".....EMPLOYEES.....", fg = 'yellow')
            click.secho('   1. Add New Employee  \n   2. View All Employees  ', fg='blue')

            employee_option = click.prompt("Select Employee Option", type=int)


    




workplace()