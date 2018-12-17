from calculator import Calculator

calc = Calculator()

calc.set_input(x=[0.52360, 0.87267, 1.22173, 1.57080, 1.91986],
               f=[0.00000, 0.00017, 0.00199, 0.01282, 0.05744])

calc.calculate()
calc.print_results()
