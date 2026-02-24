import json
import os

class Company:
    """Represents a job/internship application."""

    def __init__(self, name: str, position: str, contact_date: str, status: str):
        self.name = name
        self.position = position
        self.contact_date = contact_date
        self.status = status

    def to_dict(self) -> dict:
        """Converts the object to a dictionary for JSON serialization."""
        return vars(self)

    def __str__(self) -> str:
        return f"[{self.status.upper()}] {self.name} - {self.position} (Date: {self.contact_date})"


class Tracker:
    """Manages the list of applications and data persistence."""

    def __init__(self):
        self.applications: list[Company] = []
        self.file_path = "storage.json"

    def add_application(self, company: Company) -> None:
        """Adds a new company to the tracker."""
        self.applications.append(company)

    def display_all(self) -> None:
        """Prints all applications in the console."""
        if not self.applications:
            print("\nNo applications found.")
            return
        
        print("\n--- MY APPLICATIONS ---")
        for app in self.applications:
            print(app)

    def save_data(self) -> None:
        """Saves current applications to a JSON file."""
        data = [app.to_dict() for app in self.applications]
        
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"\nData successfully saved to {self.file_path}")

    def load_data(self) -> None:
        """Loads applications from the JSON file if it exists."""
        if not os.path.exists(self.file_path):
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                # Reconstruct Company objects from dictionaries
                self.applications = [Company(**item) for item in raw_data]
            print(f"Successfully loaded {len(self.applications)} applications.")
        except (json.JSONDecodeError, KeyError):
            print("Error: Could not parse storage.json. Starting with an empty list.")


if __name__ == "__main__":
    tracker = Tracker()
    tracker.load_data() # Loads existing data at startup
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1 : Add an application")
        print("2 : View my applications")
        print("3 : Save and Quit")
        
        choice = input("Your choice: ")
        
        match choice:
            case "1":
                name = input("Company Name: ")
                position = input("Position: ")
                date = input("Contact Date (YYYY-MM-DD): ")
                status = input("Status: ")
                new_app = Company(name, position, date, status)
                tracker.add_application(new_app)
            
            case "2":
                tracker.display_all()
            
            case "3":
                tracker.save_data()
                break 
            
            case _:
                print("Error: Please select a number between 1 and 3.")