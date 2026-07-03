from collections import defaultdict
class Twitter:

    def __init__(self):
        self.postNum = 0
        self.userToFollowing = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.postNum,tweetId])
        self.postNum -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.userToFollowing[userId].add(userId)

        for followee in self.userToFollowing[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) -1
                count , tweetId = self.tweets[followee][index]
                minHeap.append([count,tweetId,followee,index - 1])

        heapq.heapify(minHeap)
        print(minHeap)
        while minHeap and len(res) < 10:
            count,tweetId,followee,index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index > -1:
                count , tweetId = self.tweets[followee][index]
                heapq.heappush(minHeap, [count,tweetId,followee,index - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowing[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.userToFollowing[followerId]:
            self.userToFollowing[followerId].remove(followeeId) 

