# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, label=""):
    """
    Read a matrix of the given dimensions from the user, row by row.
    Each row is entered as space-separated values on one line.
    """
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}{label}: ")
            values = row_input.split()

            if len(values) != cols:
                print(f"Error: Expected {cols} values, got {len(values)}. Try again.")
                continue

            try:
                row = [float(v) for v in values]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid numbers only.")

    return matrix


def display_matrix(matrix, title="Matrix"):
    """Print a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    for row in matrix:
        formatted_row = "  ".join(f"{value:g}" for value in row)
        print(formatted_row)


def transpose_matrix(matrix):
    """
    Return the transpose of a matrix using nested loops.
    An M x N matrix becomes an N x M matrix.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


def add_matrices(matrix_a, matrix_b):
    """
    Return the element-wise sum of two matrices of the same size,
    using nested loops.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)

    return result


def multiply_matrices(matrix_a, matrix_b):
    """
    Return the matrix product A x B using nested loops.
    A is M x N, B is N x P, result is M x P.
    """
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])

    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


def get_dimensions(prompt_rows="Enter number of rows: ", prompt_cols="Enter number of columns: "):
    """Prompt for and validate positive integer dimensions."""
    while True:
        try:
            rows = int(input(prompt_rows))
            cols = int(input(prompt_cols))
            if rows <= 0 or cols <= 0:
                print("Error: Dimensions must be positive integers.")
                continue
            return rows, cols
        except ValueError:
            print("Error: Please enter valid integers.")


def part_a_transpose():
    print("\n--- PART A: Transpose a Matrix ---")
    rows, cols = get_dimensions()
    matrix = read_matrix(rows, cols)

    display_matrix(matrix, "Original Matrix")
    result = transpose_matrix(matrix)
    display_matrix(result, "Transposed Matrix")


def part_b_addition():
    print("\n--- PART B: Add Two Matrices ---")
    rows, cols = get_dimensions()

    print("\nMatrix A:")
    matrix_a = read_matrix(rows, cols)

    print("\nMatrix B (must be the same size):")
    matrix_b = read_matrix(rows, cols)

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    result = add_matrices(matrix_a, matrix_b)
    display_matrix(result, "Sum (A + B)")


def part_c_multiplication():
    print("\n--- PART C: Multiply Two Matrices ---")
    print("Matrix A dimensions (M x N):")
    m, n = get_dimensions()
    matrix_a = read_matrix(m, n, " of A")

    print("\nMatrix B dimensions (N x P) — rows must equal N:")
    n2, p = get_dimensions()

    if n2 != n:
        print(f"Error: Matrix B must have {n} rows to match Matrix A's columns.")
        return

    matrix_b = read_matrix(n2, p, " of B")

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    result = multiply_matrices(matrix_a, matrix_b)
    display_matrix(result, "Product (A x B)")


def main():
    part_a_transpose()
    part_b_addition()
    part_c_multiplication()


if __name__ == "__main__":
    main()