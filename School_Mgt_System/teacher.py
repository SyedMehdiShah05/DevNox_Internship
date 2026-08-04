class Teacher:
    def __init__(self, name, specialization, contact):
        self.name = name
        self.specialization = specialization
        self.contact = contact

    def display(self):
        return f"Name : {self.name} | Teacher: {self.specialization} | Contact : {self.contact}"

    def display_info(self):
        return self.display()