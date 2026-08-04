class Timetable:
    def __init__(self, day, timing, subject):
        self.day = day
        self.timing = timing
        self.subject = subject

    def display(self):
        return f"{self.day} at {self.timing} - {self.subject}"

    def __str__(self):
        return f"Timetable: {self.day} at {self.timing} - {self.subject}"