from admin import Admin
from user import User
from database import Database

a = Admin('mark', '12345', 3)
u = User('jimmy', 'password')

users = [a, u]
for user in users:
    user.save()

for user in users:
    print(user)

print(Database.find(lambda x: x['username']=='mark'))
print(Database.find(lambda x: x['username']=='jimmy'))





