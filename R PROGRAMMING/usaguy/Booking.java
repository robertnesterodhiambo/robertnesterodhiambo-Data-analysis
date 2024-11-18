public class Booking {
    private String bookingId;
    private Flight flight;
    private Passenger passenger;

    public Booking(String bookingId, Flight flight, Passenger passenger) {
        this.bookingId = bookingId;
        this.flight = flight;
        this.passenger = passenger;
    }

    public void displayBookingInfo() {
        System.out.println("Booking ID: " + bookingId);
        System.out.println("Flight: " + flight.getFlightNumber());
        System.out.println("Passenger: " + passenger.name);
    }
}

