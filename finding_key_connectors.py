users = (
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
)
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


def construct_friends_for_users(users, friendships):
    for user1, user2 in friendships:
        users[user1]['friends'] = users[user1].get('friends', [])
        users[user1]['friends'].append(user2)

        users[user2]['friends'] = users[user2].get('friends', [])
        users[user2]['friends'].append(user1)

    return users


print(construct_friends_for_users(users, friendships))
