def shape(matrix): return len(matrix), len(matrix[0])


def get_row(matrix, row_idx): return matrix[row_idx]


def get_col(matrix, col_idx): return [matrix[row_idx][col_idx] for row_idx in matrix]


def main():
    example_matrix = [[1, 2, 3], [4, 5, 6]]
    print(shape(example_matrix))


if __name__ == '__main__':
    main()
