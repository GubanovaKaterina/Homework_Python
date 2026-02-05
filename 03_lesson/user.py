class User:    
    
    def __init__(self, firstname, lastname):
        self.firstn = firstname
        self.lastn = lastname

    def sayfirstname(self):
        return self.firstn

    def saylastname(self):
        return self.lastn

    def sayfullname(self):
        return (f"{self.firstn} {self.lastn}")