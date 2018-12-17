class Calculator:
    def __init__(self):
        self.input = {'x': [0], 'f': [0]}
        self.results = {'f': [], 'b': []}
        pass

    def set_input(self, x, f):
        self.input['x'] = x
        self.input['f'] = f

    def calculate(self):
        self.iterate_coeff(0, len(self.input['x']) - 1)
        for elem in self.results['f']:
            if elem[0][0] == 0:
                self.results['b'].append((elem[0][1], elem[1]))

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
