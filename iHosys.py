# Simple Hospital Patient Registration (Class Demo)

# -------------------------
# Classes + Inheritance
# -------------------------
class Patient:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age
        self.paid = False   # NEW: payment status

    # Polymorphism
    def get_bill(self):
        return 0

    def show_details(self):
        status = "PAID" if self.paid else "NOT PAID"
        print(f"ID: {self.pid} | Name: {self.name} | Age: {self.age} | Status: {status}")


class Outpatient(Patient):
    def __init__(self, pid, name, age, consultation_fee):
        super().__init__(pid, name, age)
        self.consultation_fee = consultation_fee

    def get_bill(self):
        return self.consultation_fee


class Inpatient(Patient):
    def __init__(self, pid, name, age, daily_rate, days):
        super().__init__(pid, name, age)
        self.daily_rate = daily_rate
        self.days = days

    def get_bill(self):
        return self.daily_rate * self.days


# -------------------------
# Functions
# -------------------------
def register_outpatient():
    pid = input("Patient ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    fee = float(input("Consultation fee: "))
    return Outpatient(pid, name, age, fee)


def register_inpatient():
    pid = input("Patient ID: ")
    name = input("Name: ")
    age = int(input("Age: "))
    rate = float(input("Daily rate: "))
    days = int(input("Days admitted: "))
    return Inpatient(pid, name, age, rate, days)


def view_all_patients(patients):
    if not patients:
        print("No patients registered yet.")
        return

    print("\n--- All Patients ---")
    for p in patients:
        p.show_details()
        print("Bill:", p.get_bill())
        print("-------------------")


def check_patient_bill(patients):
    pid = input("Enter Patient ID: ")

    for p in patients:
        if p.pid == pid:
            print(f"Patient: {p.name}")
            print(f"Total Bill: {p.get_bill()}")
            return

    print("Patient not found.")


def pay_patient_bill(patients):
    pid = input("Enter Patient ID: ")

    for p in patients:
        if p.pid == pid:
            if p.paid:
                print("Bill has already been paid.")
            else:
                amount = p.get_bill()
                print(f"Amount to pay: {amount}")
                confirm = input("Confirm payment (yes/no): ")

                if confirm.lower() == "yes":
                    p.paid = True
                    print("Payment successful.")
                else:
                    print("Payment cancelled.")
            return

    print("Patient not found.")


# -------------------------
# Main Program (Loop + Menu)
# -------------------------
patients = []

while True:
    print("\n=== Hospital Registration Menu ===")
    print("1. Register Outpatient")
    print("2. Register Inpatient")
    print("3. View All Patients")
    print("4. Check Patient Bill")
    print("5. Pay Patient Bill")
    print("6. Exit")

    choice = input("Choose (1-6): ")

    if choice == "1":
        patients.append(register_outpatient())
        print("Outpatient registered successfully.")

    elif choice == "2":
        patients.append(register_inpatient())
        print("Inpatient registered successfully.")

    elif choice == "3":
        view_all_patients(patients)

    elif choice == "4":
        check_patient_bill(patients)

    elif choice == "5":
        pay_patient_bill(patients)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
