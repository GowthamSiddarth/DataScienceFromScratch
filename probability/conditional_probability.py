import random


def random_kid(): return random.choice(["boy", "girl"])


def main():
    both_girls, older_girl, either_girl = 0, 0, 0
    random.seed(42)
    for _ in range(10000):
        younger = random_kid()
        older = random_kid()
        if "girl" == older:
            older_girl = older_girl + 1
        if "girl" == older and "girl" == younger:
            both_girls = both_girls + 1
        if "girl" == older or "girl" == younger:
            either_girl = either_girl + 1

    print("P(both | older) = " + str(both_girls / older_girl))
    print("P(both | either) = " + str(both_girls / either_girl))


if __name__ == '__main__':
    main()
