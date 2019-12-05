class User:
    def __init__(self, email, password, name, lastname, gender, user_number=0):
        self.email = email
        self.password = password
        self.name = name
        self.lastname = lastname
        self.gender = gender
        self.user_number = user_number

    def __str__(self):
        return"| %3d | %15s | %15s | %15s | %15s | %2s |" % \
              (self.user_number, self.email, self.password, self.name, self.lastname, self.gender)
