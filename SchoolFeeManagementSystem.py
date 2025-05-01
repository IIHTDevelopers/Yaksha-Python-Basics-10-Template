import os

# Static Data: Dictionary containing student fee records
student_fees = {
    "S101": {"name": "Alice", "grade": "5th", "fees_paid": 2000, "total_fees": 5000},
    "S102": {"name": "Bob", "grade": "6th", "fees_paid": 3500, "total_fees": 5000},
    "S103": {"name": "Charlie", "grade": "7th", "fees_paid": 5000, "total_fees": 5000},
    "S104": {"name": "David", "grade": "8th", "fees_paid": 1000, "total_fees": 6000},
    "S105": {"name": "Emma", "grade": "9th", "fees_paid": 4000, "total_fees": 7000}
}

# File to store student fee records
FILE_NAME = "fees_data.txt"


def save_to_file():
    """
    Save the student fee records to a file.
    """
    pass  # TODO: Implement file writing logic


def get_fees(student_name):
    """
    Retrieve and display student's fee details from the file and return
    """
    pass  


def display_fees():
    """
    Display all student fee records from the file.
    """
    pass  # TODO: Implement logic to read and display the entire file contents


# Main Execution
def main():
    """
    Main execution function.
    """
    save_to_file()  # TODO: Implement function

    print(get_fees())  # TODO: Implement function
    print(display_fees())  # TODO: Implement function


if __name__ == "__main__":
    main()
