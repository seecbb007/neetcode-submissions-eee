class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.timer = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.timer,tweetId])
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        userlist = list(self.followMap[userId])
        userlist.append(userId)
        for uId in userlist:
            if uId in self.tweetMap:
                idx = len(self.tweetMap[uId]) - 1
                time,tid = self.tweetMap[uId][idx]
                heapq.heappush(minheap, [-time,tid,uId,idx - 1])

        while minheap and len(res) < 10:
            time,tid,uId, idx = heapq.heappop(minheap)
            res.append(tid)

            if idx >= 0:
                nextTime,nexttId = self.tweetMap[uId][idx]
                heapq.heappush(minheap, [-nextTime, nexttId, uId, idx - 1])
        return res 

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
