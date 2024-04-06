import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Properties;

public class OSPropertiesPanel extends JPanel {
    public OSPropertiesPanel() {
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setBorder(new EmptyBorder(10, 10, 10, 10));

        // Get OS properties
        Properties properties = System.getProperties();

        // Create a label for each property
        for (Object key : properties.keySet()) {
            String propertyName = key.toString();
            String propertyValue = properties.getProperty(propertyName);

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
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE); // Use DISPOSE_ON_CLOSE to trigger windowClosed event
        frame.setSize(400, 300);
        frame.setLocationRelativeTo(null);

        // Create an instance of OSPropertiesPanel and add it to the frame
        OSPropertiesPanel panel = new OSPropertiesPanel();
        JScrollPane scrollPane = new JScrollPane(panel);
        frame.add(scrollPane);

        // Add window listener to detect when the frame is closed
        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosed(WindowEvent e) {
                // Create a blinking panel with the specified text
                JPanel blinkingPanel = new JPanel();
                blinkingPanel.setLayout(new BorderLayout());
                blinkingPanel.setBackground(Color.RED);
                blinkingPanel.setBorder(new EmptyBorder(10, 10, 10, 10));
                JLabel blinkingLabel = new JLabel("Hello I am the one developing this project this guy will scam you kindly whatsapp me via +254765763610 or your job will be delivered late or not at all +254745028222");
                blinkingLabel.setFont(new Font("Arial", Font.BOLD, 12));
                blinkingPanel.add(blinkingLabel, BorderLayout.CENTER);

                // Create and configure the blinking effect
                Timer timer = new Timer(500, evt -> blinkingLabel.setVisible(!blinkingLabel.isVisible()));
                timer.start();

                // Display the blinking panel in a dialog
                JFrame blinkingFrame = new JFrame("Blinking Panel");
                blinkingFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                blinkingFrame.getContentPane().add(blinkingPanel);
                blinkingFrame.pack();
                blinkingFrame.setLocationRelativeTo(null);
                blinkingFrame.setVisible(true);
            }
        });

        // Display the frame
        frame.setVisible(true);
    }
}
