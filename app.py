import click 
from datetime import datetime
from models import Department,Position,Employee,session
from crud import add_department,add_employee,add_position,view_all_departments,view_all_employees,view_all_positions,view_department_employees,view_department_positions

def workplace():
    click.secho("Welcome To Workplace App", fg='blue', bg="white", bold=True)
    click.secho('Select an option to proceed', fg="yellow")
    click.secho('   1. Departments  \n   2. Positions  \n   3. Employees  \n   4. Exit Program', fg='blue')

    choice = click.prompt("Select Option", type=int)

    if choice not in [1, 2, 3, 4]:
        print("Invalid choice!Please select 1,2 or 3 to proceed")
        return workplace()
    if choice == 1:
        while True:
            click.secho(".....DEPARTMENTS.....", fg = 'yellow')
            click.secho('   1. Add New Departments  \n   2. View All Departments  \n   3. View Department Employees and their positions  \n   4. Back to Main Menu', fg='blue')

            department_option = click.prompt("Select Department Option", type=int)

            if department_option in[1,2,3,4]:
                break
            else:
                print("Kindly enter a valid choice!")
                continue
        if department_option == 1:
            click.secho('To add a new department...', fg='blue')
            while True:
                name = click.prompt('enter name...', type=str)
                description = click.prompt('enter description...', type=str)
                if name and description:
                    add_department(name,description)
                    click.secho('Department added successfully', fg='green')
                    return workplace()
                else:
                    click.secho('kindly enter a valid data', fg='red')
                    continue

        elif department_option == 2:
            view_all_departments()

        elif department_option == 3:
            depName = click.prompt('kindly input department name', fg='blue')
            view_department_employees(depName)
            
        elif department_option == 4:
            return workplace()            

        else:
            click.secho("Kindly enter a valid choice!", fg='red')

    elif choice == 2:
        while True:
            click.secho(".....POSITIONS.....", fg='yellow')
            click.secho(
                    '1. Add New Position\n2. View All Positions\n3. Back To Main Menu',
                    fg='blue'
                )
            position_option = click.prompt("Select Position Option", type=int)

            if position_option == 1:
                click.secho('To add a new position...', fg='blue')
                while True:
                    name = click.prompt('Enter position name', type=str)
                    description = click.prompt('Enter description', type=str)
                    department = click.prompt('Enter department name', type=str)
                    if name and description and department:
                        add_position(name, description,department)
                        click.secho('Position added successfully', fg='green')
                        break
                    else:
                        click.secho('Kindly enter valid data', fg='red')
                        continue 

            elif position_option == 2:
                view_all_positions()
            
                 

            elif position_option == 3:
                return workplace()

            else:
                click.secho("Kindly enter a valid choice!", fg='red')


    elif choice == 3:
            while True:
                click.secho(".....EMPLOYEES.....", fg='yellow')
                click.secho(
                    '1.  Add New Employee\n2.  View All Employees\n3.  Back To Main Menu',
                    fg='blue'
                )
                employee_option = click.prompt("Select Employee Option", type=int)

                if employee_option == 1:
                    click.secho('To add a new employee...', fg='blue')
                    while True:
                        first_name = click.prompt('Enter employee first name', type=str)
                        last_name = click.prompt('Enter employee last name', type=str)
                        email = click.prompt('Enter employee email', type=str)
                        position = click.prompt('Enter position', type=str)
                        department_name = click.prompt('Enter department name', type=str)

                        if first_name and last_name and email and position and department_name :
                            add_employee(first_name,last_name,email, department_name,position)
                            click.secho('Employee added successfully', fg='green')
                            break
                        else:
                            click.secho('Kindly enter valid data', fg='red')
                    continue  

                elif employee_option == 2:
                    view_all_employees()

                elif employee_option == 3:
                    return workplace()    

                else:
                    click.secho("Kindly enter a valid choice!", fg='red')

    elif choice == 4:
            click.secho("Exiting program. Goodbye!", fg='green')
            return

    else:
            click.secho("Kindly enter a valid choice!", fg='red')
            return workplace()



workplace()