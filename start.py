x = 1

from calculator import Calculator

calc = Calculator()

calc.set_input(x=[-3, -2, -1, 0, 1, 2, 3],
               f=[10, 5, 2, 1, 2, 5, 10])

calc.calculate()
calc.print_results()

print('\n{}'.format(calc.calculate_spline_at_x(x)))
