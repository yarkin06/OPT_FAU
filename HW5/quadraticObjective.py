# Optimization for Engineers - Dr.Johannes Hild
# quadratic objective
# Do not change this file

# n-dimensional quadratic function mapping x -> 0.5*x'*A*x + b'*x +c

# Class parameters:
# A: real valued matrix nxn
# b: column vector in R^n
# c: real number

# Input Definition:
# x: vector in R**n (domain space)

# Output Definition:
# objective(): real number, evaluation at x for parameters p
# gradient(): vector in R**n, evaluation of gradient wrt x
# hessian(): matrix in R**nxn, evaluation of hessian wrt x

# Required files:
# < none >

# [myValue,myGradient,myHessian]=quadraticConstraint([1;1],[1,0;0,1],[1;1],1);
# should return
# myValue=4; myGradient=[2;2]; myHessian=[1,0;0,1];

# Test cases:
# A = np.eye(2)
# b = np.ones((2,1))
# c = 1
# myObjective = quadraticObjective(A,b,c)
# y = myObjective.objective(b)
# should return y = 4

# grad = myObjective.gradient(b)
# should return grad = [[2],[2]]

# hess = myObjective.hessian(b)
# should return hess = [[1, 0],[0, 1]]

import numpy as np


def matrnr():
    # set your matriculation number here
    matrnr = 0
    return matrnr


class quadraticObjective:

    def __init__(self, A: np.array, b: np.array, c: float):
        self.A = A
        self.b = b
        self.c = c

    def objective(self, x: np.array):
        f = 0.5 * (x.T @ (self.A @ x)) + self.b.T @ x + self.c
        return f

    def gradient(self, x: np.array):
        g = self.A @ x + self.b
        return g

    def hessian(self, x: np.array):
        h = self.A
        return h
