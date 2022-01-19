from colorama import init
from termcolor import colored
import sympy as sym

print('\n')
exp =  input("Enter the expression: ")
degree = int(input("Enter the degree of differentiation: "))
print('\n')



def get_nth_derivative(exp, n):
    exp = sym.sympify(exp)
    exp_deriv = sym.diff(exp)                   
    print(colored(f'the 1st derivative is: {exp_deriv}', 'green'))
    for i in range(1, n):
        exp_deriv = sym.diff(exp_deriv)
        print(colored(f'the {i+1}th derivative is: {exp_deriv}', 'blue'))
    return exp_deriv


if __name__ == '__main__':
    sym.init_printing()
    get_nth_derivative(exp, degree) 