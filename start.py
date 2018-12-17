from calculator import Calculator

calc = Calculator()

calc.set_input(x=[-3, -2, -1, 0, 1, 2, 3],
               f=[9, 4, 1, 0, 1, 4, 9])

calc.calculate()
calc.print_results()

print(calc.p(2))
print(calc.calculate_spline_at_x(1))
