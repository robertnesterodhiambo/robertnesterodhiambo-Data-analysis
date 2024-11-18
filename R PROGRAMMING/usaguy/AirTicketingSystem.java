public class AirTicketingSystem {
    public static void main(String[] args) {
        // Initialize system components
        FlightManager flightManager = new FlightManager();
        UserManager userManager = new UserManager();
        BookingManager bookingManager = new BookingManager(flightManager, userManager);
        
        // Demo functionality (add flights, register users, make bookings)
    }
}

