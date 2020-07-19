# Reservations
import tkinter as tk


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
        
# person = Reservation('First Class', 'Middle', 2, 'yes')

# print(person)
# person.price_calc()
# print(person.seat_comfort())
# person.is_round_trip()
# print(person.get_price())

root = tk.Tk()

height = 325
width = 400

root.title("Airline Reservation")

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='airplane.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#2E9AFE')
frame.place(relx=0.06, rely=0.07, relwidth=0.9, relheight=0.55)


creator = tk.Label(
    root,
    font=('Futura', 15),
    text="Made by Program Explorers",
    foreground="#6E6E6E",  # Set the text color to white
    background="#5D8AC5"  # Set the background color to black
)
creator.place(relx=0, rely=0.92, relwidth=0.6, relheight=0.06)

class_seat_l = tk.Label(frame, text='Seat Class', bg='#336FD9', fg='#FFFFFF')
class_seat_l.grid(row=0, column=0, pady=5)

class_variable = tk.StringVar()
first_class = tk.Radiobutton(frame, text="First", variable=class_variable,
                       indicatoron=False, value="first", width=8)
business_class = tk.Radiobutton(frame, text="Business", variable=class_variable,
                          indicatoron=False, value="business", width=8)
economy_class = tk.Radiobutton(frame, text="Economy", variable=class_variable,
                          indicatoron=False, value="eco", width=8)
first_class.grid(row=0, column=1, pady=5)
business_class.grid(row=0, column=2, pady=5)
economy_class.grid(row=0, column=3, pady=5)


seat_type_l = tk.Label(frame, text='Seat Type', bg='#336FD9', fg='#FFFFFF')
seat_type_l.grid(row=1, column=0, pady=5)

seat_type_variable = tk.StringVar()
window = tk.Radiobutton(frame, text="Window", variable=seat_type_variable,
                       indicatoron=False, value="first", width=8)
middle = tk.Radiobutton(frame, text="Middle", variable=seat_type_variable,
                          indicatoron=False, value="business", width=8)
alley = tk.Radiobutton(frame, text="Alley", variable=seat_type_variable,
                          indicatoron=False, value="eco", width=8)
window.grid(row=1, column=1, pady=5)
middle.grid(row=1, column=2, pady=5)
alley.grid(row=1, column=3, pady=5)

num_seats_l = tk.Label(frame, text='Number of seats', bg='#336FD9', fg='#FFFFFF')
num_seats_l.grid(row=2, pady=5)

num_seats = tk.Scale(frame, from_=0, to=20, orient='horizontal')
num_seats.place(relx=0.3, rely=0.425, relwidth=0.66)

button = tk.Button(frame, text='Get Seats',
command=lambda: __str__(), get_price())
button.place(relx=0.22, rely=0.7, relwidth=0.55, relheight=0.2)

lower_frame = tk.Frame(root, bg='#2E9AFE')
lower_frame.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.25)


root.mainloop()



