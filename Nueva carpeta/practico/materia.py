class Subject:
    def __init__(self, name, prerequisites=None):
        self.name = name
        self.prerequisites = prerequisites or []
