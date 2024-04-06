import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.util.Map;
import java.util.Properties;

public class OSPropertiesPanel extends JPanel {
    public OSPropertiesPanel() {
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setBorder(new EmptyBorder(10, 10, 10, 10));

        // Get OS properties
        Properties properties = System.getProperties();

        // Create a label for each property
        for (Map.Entry<Object, Object> entry : properties.entrySet()) {
            String propertyName = entry.getKey().toString();
            String propertyValue = entry.getValue().toString();

            JLabel label = new JLabel("<html><b>" + propertyName + ":</b> " + propertyValue + "</html>");
            label.setAlignmentX(Component.LEFT_ALIGNMENT);
            label.setBorder(new EmptyBorder(5, 0, 5, 0));
            add(label);
        }
    }

    public static void main(String[] args) {
        // Set look and feel to Nimbus for better appearance
        try {
            UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Create and configure the frame
        JFrame frame = new JFrame("OS Properties");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLocationRelativeTo(null);

        // Create an instance of OSPropertiesPanel and add it to the frame
        OSPropertiesPanel panel = new OSPropertiesPanel();
        JScrollPane scrollPane = new JScrollPane(panel);
        frame.add(scrollPane);

        // Display the frame
        frame.setVisible(true);
    }
}