from db import PlaylistDatabase

db = PlaylistDatabase('db.json')

# print(db.add_user(1, 'user01'))
# print(db.add_playlist('workout', 3))
print(db.is_user(2))
# print((db.view_users()[0]))