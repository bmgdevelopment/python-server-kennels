# CUSTOMERS REQUEST.PY
# This file provides the information that will later be requested

import sqlite3
import json

from models import Customer

CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct",
      "animalId": 1,
      "email": "hannahhall@me.com"
    },
    {
      "id": 2,
      "name": "Seth Jehnil",
      "address": "892 Moon Way",
      "animalId": 2,
      "email": "sethjehnil@me.com"
    },
    {
      "id": 3,
      "name": "Wilen Uehsen",
      "address": "1037 Hiwnon Lane",
      "animalId": 3,
      "email": "wilenuehsen@me.com"
    },
    {
      "id": 4,
      "name": "TEST",
      "address": "1037 Test Lane",
      "animalId": 4,
      "email": "test@me.com"
    }
]

# GET ONE CUSTOMER BY ID
# -----------------------
def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS: 

        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

# GET ALL CUSTOMERS AS AN ITERABLE LIST
# -------------------------------------
# def get_all_customers():
#     return CUSTOMERS

def get_all_customers():

  with sqlite3.connect("./kennel.db") as conn: 

      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      db_cursor.execute("""
      SELECT
        a.id,
        a.name,
        a.address,
        a.email,
        a.password
      FROM customer a
      """)

      customers = []

      dataset = db_cursor.fetchall()

      for row in dataset:
        customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])
        customers.append(customer.__dict__)

  return json.dumps(customers)

# CREATE A CUSTOMER
# ------------------
def create_customer(customer):
  max_id = CUSTOMERS[-1]["id"]
  new_id = max_id + 1
  customer["id"] = new_id

  CUSTOMERS.append(customer)

  return customer


# DELETE CUSTOMER
# ----------------
def delete_customer(id):
  customer_index = -1

  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      customer_index = index

  if customer_index >= 0:
    CUSTOMERS.pop(customer_index)

# UPDATE CUSTOMER
# ----------------
def update_customer(id, new_customer):
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      CUSTOMERS[index] = new_customer
      break

