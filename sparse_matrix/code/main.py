from sparse_matrix import SparseMatrix
matrix_1_path = '../sample_input/matrixfile1.txt'
matrix_2_path = '../sample_input/matrixfile3.txt'


def main():
    import sys

    operation = input(
        "Enter operation (Add, Subtract, Multiply): ").strip().lower()
    # matrix_file1 = input("Enter the first matrix file path: ").strip()
    # matrix_file2 = input("Enter the second matrix file path: ").strip()

    matrix1 = SparseMatrix(matrix_file_path='../sample_input/matrixfile1.txt')
    matrix2 = SparseMatrix(matrix_file_path='../sample_input/matrixfile1.txt')

    if operation == "add":
        result = matrix1.add(matrix2)
    elif operation == "subtract":
        result = matrix1.subtract(matrix2)
    elif operation == "multiply":
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid operation")
        sys.exit()

    result.print_readable()

    # print(result)


if __name__ == "__main__":
    main()
