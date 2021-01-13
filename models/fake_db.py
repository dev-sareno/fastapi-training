class FakeDb():
    def __init__(self):
        self.users = [
            {
                "username": "johndoe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "password_hash": "$2y$12$QT74FqaCxQ7puSbPUOAzH.fNTPbDx2JOu8RIJxwH3TBuqN1nSi94a"  # mysecretpassword
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
                "last_name": last_name,
                "password_hash": kwargs.get("password_hash")
            }
        self.users.append(data)
    

    def get_user(self, username):
        return next((i for i in self.users if i.get("username") == username), None)
    