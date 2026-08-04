class Classroom:
    def __init__(self, class_id, capacity, room_type):
        self.class_id = class_id
        self.capacity = capacity
        self.room_type = room_type

    def display(self):
        return f"Class ID: {self.class_id} | Capacity: {self.capacity} | Room Type = {self.room_type}"

    def display_info(self):
        return self.display()