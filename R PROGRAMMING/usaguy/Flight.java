public class Flight {
    private String flightNumber;
    private String origin;
    private String destination;
    private int seatsAvailable;

    public Flight(String flightNumber, String origin, String destination, int seatsAvailable) {
        this.flightNumber = flightNumber;
        this.origin = origin;
        this.destination = destination;
        this.seatsAvailable = seatsAvailable;
    }

    // Getters and methods to update seats, display flight info
    public String getFlightNumber() {
        return flightNumber;
    }

    public String getOrigin() {
        return origin;
    }

    public String getDestination() {
        return destination;
    }

    public int getSeatsAvailable() {
        return seatsAvailable;
    }

    public void updateSeats(int seatsBooked) {
        this.seatsAvailable -= seatsBooked;
    }

    public void displayFlightInfo() {
        System.out.println("Flight " + flightNumber + " from " + origin + " to " + destination + " with " + seatsAvailable + " seats available.");
    }
}

