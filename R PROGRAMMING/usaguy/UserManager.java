import java.util.ArrayList;

public class UserManager {
    private ArrayList<User> users = new ArrayList<>();

    public void addUser(User user) {
        users.add(user);
    }

    public User getUserById(String id) {
        for (User user : users) {
            if (user.id.equals(id)) {
                return user;
            }
        }
        return null; // User not found
    }

    public void displayUsers() {
        for (User user : users) {
            user.displayInfo();
        }
    }
}

