class Twitter:

    def __init__(self):
        self.time = 0
        self.postmap = defaultdict(list)
        self.follwmap = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postmap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxheap = []
        userId_list = list(self.follwmap[userId])
        if userId not in self.follwmap[userId]:
            userId_list.append(userId) 
        
        for uid in userId_list:
            if uid in self.postmap and self.postmap[uid]:
                idx = len(self.postmap[uid]) - 1
                time,tid = self.postmap[uid][idx]
                heapq.heappush(maxheap, (-time, tid, uid, idx - 1))

        while maxheap and len(res) < 10:
            time,tid,uid,nextidx = heapq.heappop(maxheap)
            res.append(tid)
            if nextidx >= 0:
                newtime, newtid = self.postmap[uid][nextidx]
                heapq.heappush(maxheap, (-newtime,newtid, uid,nextidx - 1))
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follwmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follwmap[followerId]:
            self.follwmap[followerId].remove(followeeId)
        
