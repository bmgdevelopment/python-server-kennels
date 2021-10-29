# LOCATIONS REQUEST.PY
# This file provides the information that will later be requested

import sqlite3
import json

from models import Location

LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "500 Puppy Way"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "2092 Pawprint Drive"
    },
    {
      "name": "Nashville East",
      "address": "7294 Eilems Road",
      "id": 3
    }
]

# GET ONE LOCATION BY ID
# -----------------------
# def get_single_location(id):

#     requested_location = None

#     for location in LOCATIONS: 

#         if location["id"] == id:
#             requested_location = location

#             return requested_location


def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)


# ALL LOCATIONS AS AN ITERABLE LIST
# ----------------------------------
# def get_all_locations():

#     return LOCATIONS


def get_all_locations():
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
            a.address
        FROM location a
        """)

        # Initialize an empty list to hold all animal representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)



# CREATE NEW LOCATION
# --------------------
def create_location(location):

  max_id = LOCATIONS[-1]["id"]

  new_id = max_id + 1

  location["id"] = new_id

  LOCATIONS.append(location)

  return location


# DELETE LOCATION
# ----------------
def delete_location(id):
  location_index = -1

  for index, location in enumerate(LOCATIONS):
    if location["id"] == id:
      location_index = index

  if location_index >= 0:
    LOCATIONS.pop(location_index)


# UPDATE LOCATION
# ----------------
def update_location(id, new_location):
  
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:

            LOCATIONS[index] = new_location
            break