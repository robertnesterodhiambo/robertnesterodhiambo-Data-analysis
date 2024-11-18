public class Admin extends User {
    public Admin(String id, String name, String email) {
        super(id, name, email);
    }

    @Override
    public void displayInfo() {
        System.out.println("Admin: " + name);
    }
}

