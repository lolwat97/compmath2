from functools import reduce
from itertools import combinations
from operator import add
from operator import mul

class Calculator:
    def __init__(self):
        self.input = {'x': [0], 'f': [0]}
        self.results = {'f': [], 'b': [], 'b_sort': [], 'spline_coeff': []}
        pass

    def set_input(self, x, f):
        self.input['x'] = x
        self.input['f'] = f

    def calculate(self):
        self.iterate_coeff(0, len(self.input['x']) - 1)

        for elem in self.results['f']:
            if elem[0][0] == 0:
                self.results['b'].append((elem[0][1], elem[1]))

        sorted_coeff = sorted(self.results['b'])

        self.results['b_sort'] = [x[1] for x in sorted_coeff]
        self.results['coeffs'] = self.newton_to_alg(self.results['b_sort'])
        self.results['der_coeffs'] = list(map(lambda i: i*self.results['coeffs'][i], range(1, len(self.input['x']))))

        for i in range(0, len(self.input['x']) - 1):
            self.results['spline_coeff'].append(self.calculate_spline_coeff(i))

    def print_results(self):
        for key, value in self.results.items():
            print('{}:\n{}'.format(key, value))

    def iterate_coeff(self, n_start, n_end):
        if n_start == n_end:
            res = self.input['f'][n_start]
        else:
            diff = self.iterate_coeff(n_start + 1, n_end) - self.iterate_coeff(n_start, n_end - 1)
            res = diff / (self.input['x'][n_end] - self.input['x'][n_start])
        self.results['f'].append(((n_start, n_end), res))
        return res

    def newton_to_alg(self, b_coeff):
        def numbers_to_xs(tuple):
            return map(lambda n: self.input['x'][n], tuple)

        def array_of_tuples_to_sum_of_prods(array):
            arrx = map(numbers_to_xs, array)
            arr = map(lambda tupl: reduce(mul, tupl), arrx)
            return reduce(add, arr)

        size = len(self.results['b_sort'])

        coeff = []

        for b in self.results['b_sort']:
            coeff.append(b)

        for i in range(1, size):
            for k in range(0, size-i):
                coeff[k] += (-1)**i * b_coeff[i+k] * array_of_tuples_to_sum_of_prods(list(combinations(range(i+k), i)))

        return coeff

    def p(self, x):
        coeffs = self.results['coeffs']
        res = 0

        for i in range(len(coeffs)):
            res += coeffs[i] * x**i

        return res

    def pder(self, x):
        coeffs = self.results['der_coeffs']
        res = 0

        for i in range(len(coeffs)):
            res += coeffs[i] * (x ** i)

        return res

    def calculate_spline_coeff(self, n):
        x = self.input['x'][n]
        x1 = self.input['x'][n+1]
        xdiff = x1 - x
        xsum = x1 + x
        xsum12 = x1 + 2 * x
        xsum21 = 2*x1 + x
        xdiff31 = 3*x1 - x
        xdiff13 = x1 - 3*x

        f = self.input['f'][n]
        f1 = self.input['f'][n+1]
        fdiff = f1 - f

        pderx = self.pder(x)
        pderx1 = self.pder(x1)

        a3 = (pderx1 * xdiff - 2 * fdiff + pderx * xdiff)/(xdiff**3)
        a2 = (-1 * pderx1 * xdiff * xsum12 + 3 * fdiff * xsum - pderx * xdiff * xsum21)/(xdiff**3)
        a1 = (pderx1 * x * xsum21 * xdiff - 6 * fdiff * x * x1 + pderx * x1 * xsum12 * xdiff)/(xdiff**3)
        a0 = (-1 * pderx1 * x**2 * x1 * xdiff + f1 * x**2 * xdiff31 + f * x1**2 * xdiff13 - pderx * x * x1**2 * xdiff)/(xdiff**3)

        return [a3, a2, a1, a0]

    def calculate_spline_at_x(self, x):
        n = self.locate_x(x)
        coeffs = self.results['spline_coeff'][n]
        res = coeffs[0] * x**3 + coeffs[1] * x**2 + coeffs[2] * x + coeffs[3]
        return res

    def locate_x(self, x):
        for i in range(len(self.input['x']) - 1):
            if self.input['x'][i] <= x < self.input['x'][i + 1]:
                return i
        if x == self.input['x'][-1]:
            return len(self.input['x']) - 2
        else:
            raise Exception('X not found!')
