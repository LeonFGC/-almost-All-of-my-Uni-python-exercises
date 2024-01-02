class User:
    def __init__(self, name):
        self.name = name
        self.completed_subjects = []

    def complete_subject(self, subject):
        self.completed_subjects.append(subject)