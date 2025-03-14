class AppointmentManagement:
    def __init__(self):
        self.appointments = []

    def create_appointment(self, patient_name, doctor_name, date, time):
        appointment = {
            "id": len(self.appointments) + 1,
            "patient_name": patient_name,
            "doctor_name": doctor_name,
            "date": date,
            "time": time
        }
        self.appointments.append(appointment)
        print(f"Appointment created successfully: {appointment}")

    def read_appointments(self):
        if not self.appointments:
            print("No appointments available.")
        else:
            print("Current Appointments:")
            for appt in self.appointments:
                print(appt)

    def update_appointment(self, appointment_id, **kwargs):
        for appt in self.appointments:
            if appt["id"] == appointment_id:
                appt.update(kwargs)
                print(f"Appointment updated successfully: {appt}")
                return
        print(f"Sorry no appointment found with ID {appointment_id}.")

    def delete_appointment(self, appointment_id):
        for appt in self.appointments:
            if appt["id"] == appointment_id:
                self.appointments.remove(appt)
                print(f"Appointment with ID {appointment_id} deleted successfully.")
                return
        print(f"Sorry no appointment found with ID {appointment_id}.")

# Main code
if __name__ == "__main__":
    manager = AppointmentManagement()

    while True:
        print("\nDoctor Appointment Management System")
        print("1. Create New Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Delete Appointment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_name = input("Enter patient name: ")
            doctor_name = input("Enter doctor name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            manager.create_appointment(patient_name, doctor_name, date, time)

        elif choice == "2":
            manager.read_appointments()

        elif choice == "3":
            appointment_id = int(input("Enter appointment ID to update: "))
            print("Enter new values (leave blank to keep current value):")
            new_patient_name = input("New patient name: ")
            new_doctor_name = input("New doctor name: ")
            new_date = input("New appointment date (YYYY-MM-DD): ")
            new_time = input("New appointment time (HH:MM): ")

            updates = {}
            if new_patient_name:
                updates["patient_name"] = new_patient_name
            if new_doctor_name:
                updates["doctor_name"] = new_doctor_name
            if new_date:
                updates["date"] = new_date
            if new_time:
                updates["time"] = new_time

            manager.update_appointment(appointment_id, **updates)

        elif choice == "4":
            appointment_id = int(input("Enter appointment ID to delete: "))
            manager.delete_appointment(appointment_id)

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
