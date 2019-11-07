import random
from chapter_4.vector import dot_product
from chapter_5.describe_single_set_data import dev_from_mean


def covariance(x, y): return dot_product([dev_from_mean(x), dev_from_mean(y)]) / (len(x) - 1)


def main():
    random.seed(42)
    num_of_friends = [random.randint(1, 100) for _ in range(204)]
    random.seed(24)
    daily_minutes = [random.randint(1, 100) for _ in range(204)]

    cov_friends_minutes = covariance(num_of_friends, daily_minutes)
    print(cov_friends_minutes)


if __name__ == '__main__':
    main()
