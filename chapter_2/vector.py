from functools import reduce


def vector_add(vector_1, vector_2): return [vector_i + vector_j for vector_i, vector_j in zip(vector_1, vector_2)]


def vector_dot(vector_1, vector_2): return sum([vector_i * vector_j for vector_i, vector_j in zip(vector_1, vector_2)])


def vector_sum(vectors): return reduce(vector_add, vectors)


def scalar_multiply(vector, scalar): return [scalar * vector_i for vector_i in vector]


def dot_product(vectors): return reduce(vector_dot, vectors)


def main():
    vectors = [[1, 2, 3], [4, 5, 6]]
    sum_of_vectors = vector_sum(vectors)
    print(sum_of_vectors)

    scalar = 3
    scalar_product_with_vector = scalar_multiply(sum_of_vectors, scalar)
    print(scalar_product_with_vector)

    dot_product_of_vectors = dot_product(vectors)
    print(dot_product_of_vectors)


if __name__ == '__main__':
    main()
