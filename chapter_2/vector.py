from functools import reduce
import math


def vector_add(vector_1, vector_2): return [vector_i + vector_j for vector_i, vector_j in zip(vector_1, vector_2)]


def vector_subtract(vector_1, vector_2): return [vector_i - vector_j for vector_i, vector_j in zip(vector_1, vector_2)]


def vector_dot(vector_1, vector_2): return sum([vector_i * vector_j for vector_i, vector_j in zip(vector_1, vector_2)])


def vector_sum(vectors): return reduce(vector_add, vectors)


def scalar_multiply(vector, scalar): return [scalar * vector_i for vector_i in vector]


def dot_product(vectors): return reduce(vector_dot, vectors)


def sum_of_squares(vector): return vector_dot(vector, vector)


def magnitude(vector): return math.sqrt(sum_of_squares(vector))


def squared_distance(vector_1, vector_2): return sum_of_squares(vector_subtract(vector_1, vector_2))


def distance(vector_1, vector_2): return math.sqrt(squared_distance(vector_1, vector_2))


def main():
    vectors = [[1, 2, 3], [4, 5, 6]]
    sum_of_vectors = vector_sum(vectors)
    print(sum_of_vectors)

    scalar = 3
    scalar_product_with_vector = scalar_multiply(sum_of_vectors, scalar)
    print(scalar_product_with_vector)

    dot_product_of_vectors = dot_product(vectors)
    print(dot_product_of_vectors)

    example_vector_1 = [1, 4, 9]
    sum_of_squares_of_vector = sum_of_squares(example_vector_1)
    print(sum_of_squares_of_vector)

    magnitude_of_vector = magnitude(example_vector_1)
    print(magnitude_of_vector)

    example_vector_2 = [2, 4, 5]
    squared_distance_of_vectors = squared_distance(example_vector_1, example_vector_2)
    print(squared_distance_of_vectors)

    distance_between_vectors = distance(example_vector_1, example_vector_2)
    print(distance_between_vectors)


if __name__ == '__main__':
    main()
