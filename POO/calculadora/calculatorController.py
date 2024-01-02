class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate(self, operation, a, b):
        result = None

        if operation == "+":
            result = self.model.add(a, b)
        elif operation == "-":
            result = self.model.subtract(a, b)
        elif operation == "*":
            result = self.model.multiply(a, b)
        elif operation == "/":
            result = self.model.divide(a, b)

        self.view.display_result(result)
