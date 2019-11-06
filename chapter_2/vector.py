from functools import reduce


def vector_add(vector_1, vector_2): return [vector_i + vector_j for vector_i, vector_j in zip(vector_1, vector_2)]


def vector_sum(vectors): return reduce(vector_add, vectors)


def main():
    vectors = [[1, 2, 3], [4, 5, 6]]
    sum_of_vectors = vector_sum(vectors)
    print(sum_of_vectors)


if __name__ == '__main__':
    main()
