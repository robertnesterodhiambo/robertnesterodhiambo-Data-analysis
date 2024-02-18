from ReportTemplate import ReportTemplate
from Organization import Employee, Department

# Define a specific report template extending the ReportTemplate class
class FinancialReport(ReportTemplate):
    # Implement abstract methods to generate different parts of the report
    def generate_header(self):
        print("Financial Report Header")

    def generate_body(self):
        print("Financial Report Body")

    def generate_footer(self):
        print("Financial Report Footer")

# Create an instance of the FinancialReport class
report = FinancialReport()
# Generate the report using the template
report.generate_report()

# Create departments and employees for the organization
hr_department = Department("HR Department")
hr_department.add(Employee("Alice", "HR Manager"))
hr_department.add(Employee("Bob", "HR Assistant"))

it_department = Department("IT Department")
it_department.add(Employee("Charlie", "IT Manager"))
it_department.add(Employee("David", "Software Developer"))

# Create the organization structure
company = Department("Company")
company.add(hr_department)
company.add(it_department)

# Display the organization structure
company.display()
