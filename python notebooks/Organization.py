# Define a base class for components in the organization
class OrganizationComponent:
    # Define a method to display the component
    def display(self):
        pass

# Define a class representing individual employees
class Employee(OrganizationComponent):
    # Initialize with name and position
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Display employee information
    def display(self):
        print(f"Employee: {self.name}, Position: {self.position}")

# Define a class representing departments, which can contain employees and other departments
class Department(OrganizationComponent):
    # Initialize with name and an empty list of children
    def __init__(self, name):
        self.name = name
        self.children = []

    # Add a child component (employee or department)
    def add(self, component):
        self.children.append(component)

    # Remove a child component
    def remove(self, component):
        self.children.remove(component)

    # Display department information and its children
    def display(self):
        print(f"Department: {self.name}")
        for child in self.children:
            child.display()
