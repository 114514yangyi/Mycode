import numpy as np
import argparse
import sys
def matrix_multiply(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

def matrix_add(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def matrix_subtract(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def matrix_transpose(matrix):
    return np.transpose(matrix)

def matrix_inverse(matrix):
    return np.linalg.inv(matrix)

def main():
    parser = argparse.ArgumentParser(description='Matrix operations')
    parser.add_argument('operation', choices=['m', 'a', 's', 't', 'i'], help='Matrix operation')
    parser.add_argument('matrix1', type=str, help='Path to the first matrix file')
    parser.add_argument('matrix2', type=str, nargs='?', help='Path to the second matrix file (for multiply, add, and subtract operations)')
    args = parser.parse_args()

    matrix1 = np.loadtxt(args.matrix1)
    if args.operation != 't' and args.operation != 'i':
        matrix2 = np.loadtxt(args.matrix2)

    if args.operation == 'm':
        result = matrix_multiply(matrix1, matrix2)
    elif args.operation == 'a':
        result = matrix_add(matrix1, matrix2)
    elif args.operation == 's':
        result = matrix_subtract(matrix1, matrix2)
    elif args.operation == 't':
        result = matrix_transpose(matrix1)
    elif args.operation == 'i':
        result = matrix_inverse(matrix1)

    np.savetxt(sys.stdout, result, delimiter=' ')
if __name__ == '__main__':
    main()
