
with open('users.csv',  encoding='utf-8') as users, open('hobby.csv',  encoding='utf-8') as hobbies:
    users_hobbies = {}

    for u, h in zip(users, hobbies):
        user = u.split(',')
        hobby = h.split(',')
        print(user, hobby)
        user[-1] = user[-1].rstrip()
        hobby[-1] = hobby[-1].rstrip()
        users_hobbies.setdefault(' '.join(user), ','.join(hobby))

    for key, val in users_hobbies.items():

        print(key, val)
print(users_hobbies)
users_hobbies.get()
