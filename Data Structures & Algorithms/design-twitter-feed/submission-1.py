from collections import defaultdict
class Twitter:

    def __init__(self):
        # self.numOfPosts = 0
        self.userToFollowing = defaultdict(set)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId,userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        added = 0
        
        for i in range(len(self.tweets) - 1 , -1 ,-1):
            if added == 10:
                break
            
            tweetId = self.tweets[i][0]
            user = self.tweets[i][1]

            if user == userId or user in self.userToFollowing[userId]:
                posts.append(tweetId)
                added+=1
        
        return posts


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.userToFollowing[followerId]:
            self.userToFollowing[followerId].remove(followeeId) 

