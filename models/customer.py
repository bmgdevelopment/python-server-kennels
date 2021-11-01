# class Customer():

#     def __init__(self, id, name, address, animalId, email):
#         self.id = id
#         self.name = name
#         self.address = address
#         self.animalId = animalId
#         self.email = email

class Customer():

    def __init__(self, id, name, address, email = "", password = ""):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
