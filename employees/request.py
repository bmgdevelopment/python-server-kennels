# EMPLOYEES REQUEST.PY
# This file provides the information that will later be requested

import sqlite3
import json

from models import Employee

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

# GET ONE EMPLOYEE BY ID
# -----------------------
def get_single_employee(id):

    requested_employee = None
    
    for employee in EMPLOYEES:

        if employee["id"] == id: 

            requested_employee = employee

        return requested_employee 



# def get_single_employee(id):
#     with sqlite3.connect("./kennel.db") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()
#
#         # Use a ? parameter to inject a variable's value
#         # into the SQL statement.
#         db_cursor.execute("""
#         SELECT
#             a.id,
#             a.name,
#             a.address,
#             a.location_id
#         FROM employee a
#         WHERE a.id = ?
#         """, (id, ))
#
#         # Load the single result into memory
#         data = db_cursor.fetchone()
#
#         # Create an employee instance from the current row
#         employee = Employee(data['id'], data['name'], data['address'],
#                         data['location_id'])
#
#         return json.dumps(employee.__dict__)


# GET ALL EMPLOYEES AS AN ITERABLE LIST
# --------------------------------------
# def get_all_employees():
#     return EMPLOYEES


def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
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
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'])

            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)


# CREATE AN EMPLOYEE
# -------------------
def create_employee(employee):
  max_id = EMPLOYEES[-1]["id"]

  new_id = max_id + 1

  employee["id"] = new_id

  EMPLOYEES.append(employee)

  return employee

  
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