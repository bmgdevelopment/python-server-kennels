# LOCATIONS REQUEST.PY
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
    },
    {
      "id": 4,
      "name": "Testing Location",
      "address": "123 FAKE ST"
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