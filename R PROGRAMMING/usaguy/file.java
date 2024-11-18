import java.util.ArrayList;

// Main class for the air ticketing system
public class AirTicketingSystem {
    public static void main(String[] args) {
        // Initialize system components
        FlightManager flightManager = new FlightManager();
        UserManager userManager = new UserManager();
        BookingManager bookingManager = new BookingManager(flightManager, userManager);

        // Add some flights
        flightManager.addFlight(new Flight("AI202", "New York", "London", 100));
        flightManager.addFlight(new Flight("AI303", "Los Angeles", "Tokyo", 150));

        // Add some users
        userManager.addUser(new Passenger("P001", "John Doe", "john.doe@example.com"));
        userManager.addUser(new Admin("A001", "Alice Admin", "alice.admin@example.com"));

        // Display all flight information
        System.out.println("Available Flights:");
        for (Flight flight : flightManager.getFlights()) {
            flight.displayFlightInfo();
        }

        // Create a booking for a passenger
        bookingManager.createBooking("AI202", "P001");

        // Try to book a flight with no available seats
        flightManager.getFlights().get(0).bookSeat(); // Simulate seat being booked
        bookingManager.createBooking("AI202", "P001");

        // Cancel a booking
        bookingManager.cancelBooking("B1");
    }
}

// Abstract User class
abstract class User {
    protected String id;
    protected String name;
    protected String email;

    public User(String id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    public abstract void displayInfo();
}

// Passenger class
class Passenger extends User {
    public Passenger(String id, String name, String email) {
        super(id, name, email);
    }

    @Override
    public void displayInfo() {
        System.out.println("Passenger: " + name);
    }
}

// Admin class
class Admin extends User {
    public Admin(String id, String name, String email) {
        super(id, name, email);
    }

    @Override
    public void displayInfo() {
        System.out.println("Admin: " + name);
    }
}

// Flight class
class Flight {
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

    public void bookSeat() {
        if (seatsAvailable > 0) {
            seatsAvailable--;
            System.out.println("Seat booked on flight " + flightNumber);
        } else {
            System.out.println("No seats available on flight " + flightNumber);
        }
    }

    public void cancelSeat() {
        seatsAvailable++;
    }

    public void displayFlightInfo() {
        System.out.println("Flight Number: " + flightNumber + ", Origin: " + origin + ", Destination: " + destination + ", Seats Available: " + seatsAvailable);
    }
}

// FlightManager class
class FlightManager {
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
        return null; // Flight not found
    }

    public ArrayList<Flight> getFlights() {
        return flights;
    }
}

// Booking class
class Booking {
    private String bookingId;
    private Flight flight;
    private Passenger passenger;

    public Booking(String bookingId, Flight flight, Passenger passenger) {
        this.bookingId = bookingId;
        this.flight = flight;
        this.passenger = passenger;
    }

    // Getter methods for bookingId and flight
    public String getBookingId() {
        return bookingId;
    }

    public Flight getFlight() {
        return flight;
    }

    public void displayBookingInfo() {
        System.out.println("Booking ID: " + bookingId + ", Flight: " + flight.getFlightNumber() + ", Passenger: " + passenger.name);
    }
}

// BookingManager class
class BookingManager {
    private FlightManager flightManager;
    private UserManager userManager;
    private ArrayList<Booking> bookings = new ArrayList<>();

    public BookingManager(FlightManager flightManager, UserManager userManager) {
        this.flightManager = flightManager;
        this.userManager = userManager;
    }

    public void createBooking(String flightNumber, String passengerId) {
        Flight flight = flightManager.searchFlight(flightNumber);
        Passenger passenger = (Passenger) userManager.searchUser(passengerId);

        if (flight != null && passenger != null && flight.getSeatsAvailable() > 0) {
            flight.bookSeat();
            Booking booking = new Booking("B" + (bookings.size() + 1), flight, passenger);
            bookings.add(booking);
            booking.displayBookingInfo();
        } else {
            System.out.println("Booking failed: Flight not available or Passenger not found.");
        }
    }

    public void cancelBooking(String bookingId) {
        for (Booking booking : bookings) {
            if (booking.getBookingId().equals(bookingId)) {
                booking.getFlight().cancelSeat();
                bookings.remove(booking);
                System.out.println("Booking cancelled: " + bookingId);
                return;
            }
        }
        System.out.println("Booking not found for cancellation.");
    }
}

// UserManager class
class UserManager {
    private ArrayList<User> users = new ArrayList<>();

    public void addUser(User user) {
        users.add(user);
    }

    public User searchUser(String userId) {
        for (User user : users) {
            if (user.id.equals(userId)) {
                return user;
            }
        }
        return null; // User not found
    }
}
