from collections import defaultdict


def get_tenure_class(tenure):
    if tenure < 2:
        return 'less than 2 years'
    elif tenure < 5:
        return 'between 2 and 5 years'
    else:
        return 'more than 5 years'


def get_salaries_per_tenure(salaries_and_tenures):
    salaries_per_tenure = defaultdict(list)

    for salary, tenure in salaries_and_tenures:
        salaries_per_tenure[get_tenure_class(tenure)].append(salary)

    return salaries_per_tenure


def main():
    salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                            (48000, 0.7), (76000, 6),
                            (69000, 6.5), (76000, 7.5),
                            (60000, 2.5), (83000, 10),
                            (48000, 1.9), (63000, 4.2)]

    salaries_per_tenure = get_salaries_per_tenure(salaries_and_tenures)
    print(salaries_per_tenure)


if __name__ == '__main__':
    main()
