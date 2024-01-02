class Patient:
    def __init__(self, name, age, id, sex, weight, height):
        self.name = name
        self.age = age
        self.id = id
        self.sex = sex
        self.weight = weight
        self.height = height
        self.previous_weight = weight

    def get_patients_over_18(self, patients):
        return [patient for patient in patients if patient.age > 18]
    










    