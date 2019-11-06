def shape(matrix): return len(matrix), len(matrix[0])


def main():
    example_matrix = [[1, 2, 3], [4, 5, 6]]
    print(shape(example_matrix))


if __name__ == '__main__':
    main()
