class SubjectManager:
    def __init__(self):
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_subject(self, name):
        for subject in self.subjects:
            if subject.name == name:
                return subject
        return None