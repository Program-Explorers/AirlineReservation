# Reservation
import tkinter


class Reservation:
    first_num_seats = 20
    business_num_seats = 50
    eco_num_seats = 200

    def __init__(self, class_seat, seat, num_seats, round_trip):
        self.class_seat = class_seat
        self.seat = seat
        self.num_seats = num_seats
        self.comfort = 'placeholder'
        self.round_trip = round_trip
        self.cost = 0

    def __str__(self):
        return f"You requested {self.num_seats} seats, a {self.seat} seat, in {self.class_seat}"

    def seat_comfort(self):
        if self.class_seat == 'First Class':
            return "Cozy"

        elif self.class_seat == 'Business Class':
            return "Comfortable"

        else:
            return "Fine"

    def price_calc(self):
        if self.class_seat == 'First Class':
            self.cost += 1200

        elif self.class_seat == 'Business Class':
            self.cost += 660

        else:
            self.cost += 200

    def is_round_trip(self):
        if self.round_trip == 'yes':
            self.cost = self.cost * 2 - 100

    def get_price(self):
        return self.cost * self.num_seats


person = Reservation('First Class', 'Middle', 2, 'yes')

print(person)
person.price_calc()
print(person.seat_comfort())
person.is_round_trip()
print(person.get_price())



