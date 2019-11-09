import random
from linear_algebra.vector import dot_product
from statistics.describe_single_set_data import dev_from_mean, standard_deviation


def covariance(x, y): return dot_product([dev_from_mean(x), dev_from_mean(y)]) / (len(x) - 1)


def correlation(x, y):
    std_dev_x, std_dev_y = standard_deviation(x), standard_deviation(y)
    return covariance(x, y) / std_dev_x / std_dev_y if std_dev_x > 0 and std_dev_y > 0 else 0


def main():
    random.seed(42)
    num_of_friends = [random.randint(1, 100) for _ in range(204)]
    random.seed(24)
    daily_minutes = [random.randint(1, 100) for _ in range(204)]

    cov_friends_minutes = covariance(num_of_friends, daily_minutes)
    print(cov_friends_minutes)

    corr_friends_minutes = correlation(num_of_friends, daily_minutes)
    print(corr_friends_minutes)


if __name__ == '__main__':
    main()
