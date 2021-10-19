# CUSTOMERS REQUEST.PY
# This file provides the information that will later be requested

from animals import request


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
def get_all_customers():
    return CUSTOMERS


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