import java.util.ArrayList;

public class BookingManager {
    private FlightManager flightManager;
    private UserManager userManager;
    private ArrayList<Booking> bookings = new ArrayList<>();

    public BookingManager(FlightManager flightManager, UserManager userManager) {
        this.flightManager = flightManager;
        this.userManager = userManager;
    }

    public void createBooking(String flightNumber, String passengerId) {
        Flight flight = flightManager.searchFlight(flightNumber);
        Passenger passenger = (Passenger) userManager.getUserById(passengerId);
        if (flight != null && passenger != null && flight.getSeatsAvailable() > 0) {
            String bookingId = "B" + System.currentTimeMillis();
            Booking booking = new Booking(bookingId, flight, passenger);
            bookings.add(booking);
            flight.updateSeats(1); // Reserve 1 seat
            System.out.println("Booking created: " + bookingId);
        } else {
            System.out.println("Booking could not be created.");
        }
    }

    public void cancelBooking(String bookingId) {
        for (Booking booking : bookings) {
            if (bookingId.equals(booking.bookingId)) {
                bookings.remove(booking);
                booking.flight.updateSeats(-1); // Release the seat
                System.out.println("Booking cancelled: " + bookingId);
                return;
            }
        }
        System.out.println("Booking not found.");
    }
}

