import random


def main():
    num_of_friends = [random.randint(1, 100) for _ in range(100)]
    print(num_of_friends)


if __name__ == '__main__':
    main()
