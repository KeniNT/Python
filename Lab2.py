import csv

class Train:
    def __init__(self, train_id, train_name, source_station, destination_station, total_seats, fare_per_seat):
        self.train_id = train_id
        self.train_name = train_name
        self.source_station = source_station
        self.destination_station = destination_station
        self.total_seats = total_seats
        self.fare_per_seat = fare_per_seat
        self.available_seats = total_seats
        self.revenue = 0

    def check_availability(self, num_tickets):
        return self.available_seats >= num_tickets

    def book_tickets(self, num_tickets):
        if self.check_availability(num_tickets):
            self.available_seats -= num_tickets
            booking_fare = num_tickets * self.fare_per_seat
            self.revenue += booking_fare
            return True, booking_fare
        else:
            return False, 0

def load_trains(file_path):  # Corrected parameter name
    trains = {}
    with open('trains.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            train = Train(
                row['TrainID'],
                row['TrainName'],
                row['SourceStation'],
                row['DestinationStation'],
                int(row['TotalSeats']),
                int(row['FarePerSeat'])
            )
            trains[train.train_id] = train
    return trains

def load_passengers(file_path):  # Corrected parameter name
    passengers = []
    with open('passangers.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            passengers.append({
                'name': row['PassengerName'],
                'train_id': row['TrainID'],
                'num_tickets': int(row['NumberOfTickets'])
            })
    return passengers

def generate_train_report(trains):
    print("\n--- Train Report ---")
    for train in trains.values():
        print(f"Train ID: {train.train_id}, Name: {train.train_name}, From: {train.source_station} To: {train.destination_station}, Available Seats: {train.available_seats}")

def generate_revenue_report(trains):
    print("\n--- Revenue Report ---")
    for train in trains.values():
        print(f"Train ID: {train.train_id}, Name: {train.train_name}, Total Revenue: {train.revenue}")

def main():
    # Load train and passenger data
    trains = load_trains('trains.csv')
    passengers = load_passengers('passengers.csv')

    # Process each passenger's booking
    for passenger in passengers:
        train_id = passenger['train_id']
        num_tickets = passenger['num_tickets']

        if train_id not in trains:
            print(f"Error: Invalid train ID {train_id} for passenger {passenger['name']}")
            continue

        train = trains[train_id]
        success, fare = train.book_tickets(num_tickets)
        if success:
            print(f"{passenger['name']} successfully booked {num_tickets} ticket(s) on {train.train_name}. Total fare: {fare}")
        else:
            print(f"Error: Not enough seats available for {passenger['name']} on {train.train_name}")

    # Generate reports
    generate_train_report(trains)
    generate_revenue_report(trains)

if __name__ == "__main__":
    main()
