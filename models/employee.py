class Employee():

    def __init__(self, id, name, address, location_id, animal_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.animal_id = animal_id
        self.location = None
        self.animal = None
        
# TypeError: __init__() takes 4 positional arguments but 5 were given
# needed location_id to resemble the same spelling as within the kennel.sql
# not locationId like in employees/request.py
