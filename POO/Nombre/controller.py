from model import Patient

class PatientController:

    def load_patients(self, filename):
        patients = []
        with open(filename, 'r') as file:
            for line in file:
                name, age, id, sex, weight, height = line.strip().split(';')
                patient = Patient(name, int(age), id, sex, float(weight), float(height))
                patients.append(patient)
        return patients

    def get_patients_over_18(self, patients):
        return [patient for patient in patients if patient.age > 18]

    def select_patient(self, nWeight, selected_patient, patients):
        for patient in patients:
            if selected_patient == patient.name:
                patient.previous_weight = patient.weight
                patient.weight = nWeight

    def calculate_bmi(self, selected_patient, patients):
        for patient in patients:
            if selected_patient == patient.name:
                bmi = patient.weight / (patient.height ** 2)
                return (bmi)

    def calculate_difference(self, selected_patient, patients):
        for patient in patients:
            if selected_patient == patient.name:
                return patient.weight - patient.previous_weight

    def save_new_data(self, patients, filename):
        with open(filename, 'w') as file:
            for patient in patients:
                line = f"{patient.name}, {patient.age}, {patient.id}, {patient.sex}, {patient.weight}, {patient.height}\n"
                file.write(line)
                


