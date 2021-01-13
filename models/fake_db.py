class FakeDb():
    def __init__(self):
        self.users = [
            {
                "username": "johndoe@example.com",
                "first_name": "John",
                "last_name": "Doe"
            }
        ]
        
    
    def get_users(self):
        return self.users

    
    def is_username_existed(self, username):
        for user in self.users:
            if user.get("username") == username:
                return True
        
        return False

    
    def save_user(self, username, first_name, last_name, **kwargs):
        data = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name
            }
        self.users.append(data)
    