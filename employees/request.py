# EMPLOYEES REQUEST.PY
# This file provides the information that will later be requested

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

    request_employee = None
    
    for employee in EMPLOYEES:

        if employee["id"] == id: 

            requested_employee = employee

        return request_employee 


# GET ALL EMPLOYEES AS AN ITERABLE LIST
# --------------------------------------
def get_all_employees():
    return EMPLOYEES


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