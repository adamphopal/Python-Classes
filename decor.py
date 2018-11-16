#decorators
#throw an exception if trying to access data only for logged in users:
from contextlib import wraps
class User:
    
    
    is_authenicated = False

    def __init__(self, name):
        self.name = name

    def enforce_authentication(func):
        def wrapper(user):
            if not user.is_authenicated:
                raise Exception('User must login')
            return func(user)
        return wrapper

    @enforce_authentication
    def display_profile_page(user):
        print('profile: %s' % user.name)


user1 = User('hamim')
user2 = User('adam')
#print(user1.name)
print(user1.display_profile_page)
user3.display_profile_page



