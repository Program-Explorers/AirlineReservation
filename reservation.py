# Reservation
import tkinter


class Reservation():
    first_num_seats = 20
    business_num_seats = 50
    eco_num_seats = 200

    def __init__(self, class_seat, seat, num_seats):
        self.class_seat = class_seat
        self.seat = seat
        self.num_seats = num_seats
        self.comfort = 'placeholder'
        self.cost = 0

    def show(self):
        return f"You requested {self.num_seats} seats, a {self.seat} seat, in {self.class_seat}"

    def comfort(self):
        if self.class_seat == 'First Class':
            return "Cozy"

        elif self.class_seat == 'Business Class':
            return "Comfortable"

        else:
            return "Fine"

    def getprice(self):
        if self.class_seat == 'First Class':
            self.cost += 1200

        elif self.class_seat == 'Business Class':
            self.cost += 660

        else:
            self.cost += 200

        return self.cost


person = Reservation('First Class', 'Middle', 1)

print(person.show())

#person.comfort()

print(person.getprice())

