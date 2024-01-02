class View:
    def menu(self):
        print('1) to show all patiernts over 18 years old')
        print('2) to update the weight of a patient')
        print('3) to close the program')

        
    def display_patients(self, patients):
        if patients:
            print("Patients over 18 years old:")
            for patient in patients:
                print(f"Name: {patient.name}, Age: {patient.age}, ID: {patient.id}, Sex: {patient.sex}, Weight: {patient.weight}, Height: {patient.height}")
        else:
            print("No patients found")

    def choose_patient(self):
        print("Enter patient's name")
        
    def new_weight(self):
        print('Instert new weight')


    def display_bmi_result(self, bmi):
        print(f"BMI: {bmi}")

    def display_weight_difference(self, difference):
        print(f"Weight difference: {difference}")

    def bye_bye(self):
        print('Closing program')















