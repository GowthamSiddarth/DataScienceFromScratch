import random
from collections import Counter
from matplotlib import pyplot as plt


def plot_friends_vs_people(num_of_friends, num_of_people):
    friends_count = Counter(num_of_friends)
    xs = num_of_people
    ys = [friends_count[x] for x in xs]
    plt.bar(xs, ys)
    plt.axis([0, 101, 0, 25])
    plt.title("Histogram of friends count")
    plt.xlabel("# of friends")
    plt.ylabel("# of people")
    plt.draw()


def mean(num_of_friends): return sum(num_of_friends) / len(num_of_friends)


def main():
    random.seed(42)
    num_of_friends = [random.randint(1, 204) for _ in range(100)]
    num_of_people = range(101)
    plot_friends_vs_people(num_of_friends, num_of_people)

    mean_num_of_friends = mean(num_of_friends)
    print(mean_num_of_friends)
    plt.show()


if __name__ == '__main__':
    main()
