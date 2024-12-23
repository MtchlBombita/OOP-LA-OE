class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        pass

    def post(self):
        pass

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, followers):
        super().__init__(username, password)
        self.followers = followers

    def share_story(self):
        pass

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, tweets):
        super().__init__(username, password)
        self.tweets = tweets

    def tweet(self):
        pass

user1 = InstagramAccount("xshxngg", "12345678", 10000)
user2 = TwitterAccount("ashongers", "ABCDEFG", 5000)


