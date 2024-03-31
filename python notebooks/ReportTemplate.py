from abc import ABC, abstractmethod

# Define an abstract class representing the template for generating reports
class ReportTemplate(ABC):
    # Define a method to generate a report
    def generate_report(self):
        # Call abstract methods to generate different parts of the report
        self.generate_header()
        self.generate_body()
        self.generate_footer()

    # Define abstract methods for generating header, body, and footer of the report
    @abstractmethod
    def generate_header(self):
        pass

    @abstractmethod
    def generate_body(self):
        pass

    @abstractmethod
    def generate_footer(self):
        pass
