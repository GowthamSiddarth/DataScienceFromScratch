from collections import Counter, defaultdict


def construct_friends_for_users(users, friendships):
    for user1, user2 in friendships:
        users[user1]['friends'] = users[user1].get('friends', [])
        users[user1]['friends'].append(user2)

        users[user2]['friends'] = users[user2].get('friends', [])
        users[user2]['friends'].append(user1)

    return users


def get_friends_of_friends(user_id, users):
    return Counter(friend_of_friend for friend in users[user_id]['friends']
                   for friend_of_friend in users[friend]['friends'] if user_id != friend_of_friend and
                   friend_of_friend not in users[user_id]['friends'])


def get_interests_per_user(interests):
    interests_per_user = defaultdict(list)
    for user_id, interest in interests:
        interests_per_user[user_id].append(interest)

    return interests_per_user


def get_users_per_interest(interests):
    users_per_interest = defaultdict(list)

    for user_id, interest in interests:
        users_per_interest[interest].append(user_id)

    return users_per_interest


def main():
    users = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {'id': 4, 'name': "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"}
    ]
    friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                   (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
    interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
        (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
        (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
        (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"),
        (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
        (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
        (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
        (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
        (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data")
    ]

    users = construct_friends_for_users(users, friendships)
    example_user = users[3]
    friends_of_friends_example_user = get_friends_of_friends(example_user['id'], users)
    print(friends_of_friends_example_user)

    interests_per_user = get_interests_per_user(interests)
    print(interests_per_user)

    users_per_interest = get_users_per_interest(interests)
    print(users_per_interest)


if __name__ == '__main__':
    main()
