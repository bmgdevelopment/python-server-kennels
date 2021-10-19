# LOCATIONS REQUEST.PY
# This file provides the information that will later be requested

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
def get_single_location(id):

    requested_location = None

    for location in LOCATIONS: 

        if location["id"] == id:
            requested_location = location

            return requested_location


# ALL LOCATIONS AS AN ITERABLE LIST
# ----------------------------------
def get_all_locations():

    return LOCATIONS


# CREATE NEW LOCATION
# --------------------
def create_location(location):

  max_id = LOCATIONS[-1]["id"]

  new_id = max_id + 1

  location["id"] = new_id

  LOCATIONS.append(location)

  return location