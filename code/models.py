class User:
    def __init__(self, name, password, email, gender, tel, area, occupation, photo):
        self.name = name
        self.password = password
        self.email = email
        self.gender = gender
        self.tel = tel
        self.area = area
        self.occupation = occupation
        self.photo = photo
        
        pass

    def login(self):
        self.is_active = True
        pass
    def logout(self):
        self.is_active = False
        pass