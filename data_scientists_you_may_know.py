import functools
from collections import Counter


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

    users = construct_friends_for_users(users, friendships)
    example_user = users[3]
    friends_of_friends_example_user = get_friends_of_friends(example_user['id'], users)
    print(friends_of_friends_example_user)


if __name__ == '__main__':
    main()
