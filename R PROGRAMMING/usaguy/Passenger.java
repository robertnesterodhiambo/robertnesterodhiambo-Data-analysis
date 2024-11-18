public class Passenger extends User {
    public Passenger(String id, String name, String email) {
        super(id, name, email);
    }

    @Override
    public void displayInfo() {
        System.out.println("Passenger: " + name);
    }
}

