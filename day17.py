class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0  # Count of people following this user
        self.following = 0  # Count of people this user follows

    def follow(self, other_user):
        """Method to follow another user and update both profiles"""
        other_user.followers += 1
        self.following += 1

# 1. Create instances of User
user1 = User(101, "John")
user2 = User(102, "Doe")

# 2. Display initial details
print(f"Initial - {user1.name} (ID: {user1.id}): {user1.followers} followers, {user1.following} following")
print(f"Initial - {user2.name} (ID: {user2.id}): {user2.followers} followers, {user2.following} following")

# 3. Perform the follow action
print(f"\n--- {user1.name} follows {user2.name} ---")
user1.follow(user2)

# 4. Display updated details
print(f"{user1.name} stats: {user1.followers} followers, {user1.following} following")
print(f"{user2.name} stats: {user2.followers} followers, {user2.following} following")
