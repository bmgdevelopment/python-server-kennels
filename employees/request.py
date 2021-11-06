# EMPLOYEES REQUEST.PY
# This file provides the information that will later be requested

import sqlite3
import json

from models import Employee
from models import Location
from models import Animal

EMPLOYEES = [
    {
      "id": 1,
      "name": "Jeremy Baker",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Sally Wood",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Carma Reddy",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Ignatius Salvarez",
      "locationId": 2
    },
    {
      "name": "Brittany Garrett",
      "locationId": 3,
      "id": 5
    },
    {
      "name": "John Smith",
      "locationId": 3,
      "id": 6
    }
]


def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id,
            a.animal_id
        FROM employee a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                        data['location_id'], data['animal_id'])

        return json.dumps(employee.__dict__)


def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            e.animal_id,
            l.name location_name,
            l.address location_address,
            a.name animal_name,
            a.breed,
            a.customer_id,
            a.status
        FROM Employee e
        JOIN Location l
        ON l.id = e.location_id
        JOIN Animal a
        ON a.id = e.animal_id
        """)

        # Initialize an empty list to hold all animal representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class above.
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'], row['animal_id'])

           # Create a Location instance from the current row
            location = Location(row['location_id'], row['location_name'], row['location_address'])

            # Add the dictionary representation of the location to the animal
            employee.location = location.__dict__

           # Create an Animal instance from the current row
            animal = Animal(row['animal_id'], row['animal_name'], row['breed'], row['status'], row['location_id'], row['customer_id'])

            # Add the dictionary representation of the animal to the animal
            employee.animal = animal.__dict__

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)


# CREATE AN EMPLOYEE
# -------------------
def create_employee(new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id, animal_id )
        VALUES
            ( ?, ?, ?, ? );
        """, (new_employee['name'], new_employee['address'], new_employee['location_id'], new_employee['animal_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_employee['id'] = id

    return json.dumps(new_employee)

  
# DELETE AN EMPLOYEE
# -------------------
def delete_employee(id):
  employee_index = -1

  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id: 
      employee_index = index

  if employee_index >= 0:
    EMPLOYEES.pop(employee_index)


# UPDATE EMPLOYEE
# ---------------
def update_employee(id, new_employee): 
  for index, employee in enumerate(EMPLOYEES):
    if employee["id"] == id: 
      EMPLOYEES[index] = new_employee
      break

# GET EMPLOYEES BY LOCATION
# ---------------------------

def get_employees_by_locationId(location_id):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        # a.* also works within select for all keys
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id
        from Employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
