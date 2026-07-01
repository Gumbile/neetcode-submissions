from collections import defaultdict
class Twitter:

    def __init__(self):
        self.postNum = 0
        self.userToFollowing = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.postNum,tweetId])
        self.postNum+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        self.userToFollowing[userId].add(userId)
        # print(f"user {userId} : {self.userToFollowing[userId]}")
        for user in self.userToFollowing[userId]:
            userTweets = self.tweets[user]
            cnt = 0
            for tweet in range(len(userTweets) -1 , -1, -1):
                if cnt == 10:
                    break
                cnt+=1
                posts.append(userTweets[tweet])
        
        posts.sort(reverse=True)
        cnt = 0
        res = []
        
        for post in posts:
            if cnt == 10:
                break
            cnt += 1
            res.append(post[1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.userToFollowing[followerId]:
            self.userToFollowing[followerId].remove(followeeId) 

