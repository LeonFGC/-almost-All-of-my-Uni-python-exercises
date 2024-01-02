from calculatorController import CalculatorController
from calculatorModel import Calculator
from calculatorView import CalculatorView

model = Calculator()
view = CalculatorView()
controller = CalculatorController(model, view)

controller.calculate("+", 5, 3)
controller.calculate("-", 8, 2)
controller.calculate("*", 4, 6)
controller.calculate("/", 10, 2)
controller.calculate("/", 5, 0)

j=int(input())
k=int(input())
l=input()

controller.calculate(l,j,k)


