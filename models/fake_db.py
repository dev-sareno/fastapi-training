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