"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    current_number = 0
    seats = ["A", "B", "C", "D"]
    while current_number < number:
        yield seats[current_number%4]
        current_number += 1


def generate_seats(number):
    seats = ["A", "B", "C", "D"]
    current_number = 0
    skipped_row = 13

    while current_number < number:
        row = current_number // 4 + 1
        if row >= skipped_row:
            row += 1  # skip row 13
        yield f"{row}{seats[current_number % 4]}"
        current_number += 1

def assign_seats(passengers):
    seats = generate_seats(len(passengers))
    return {p: next(seats) for p in passengers}


def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        code = seat + flight_id
        number_of_zeros = 12 - len(code)
        yield code + "0" * number_of_zeros
