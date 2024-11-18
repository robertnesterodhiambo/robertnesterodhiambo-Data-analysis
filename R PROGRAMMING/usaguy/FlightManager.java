import java.util.ArrayList;

public class FlightManager {
    private ArrayList<Flight> flights = new ArrayList<>();

    public void addFlight(Flight flight) {
        flights.add(flight);
    }

    public Flight searchFlight(String flightNumber) {
        for (Flight flight : flights) {
            if (flight.getFlightNumber().equals(flightNumber)) {
                return flight;
            }
        }
        return null; // No flight found
    }

    public void displayFlights() {
        for (Flight flight : flights) {
            flight.displayFlightInfo();
        }
    }
}

