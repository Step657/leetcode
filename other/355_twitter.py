"""
355. 设计推特
    设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。
    你的设计需要支持以下的几个功能：
        postTweet(userId, tweetId): 创建一条新的推文
        getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
        follow(followerId, followeeId): 关注一个用户
        unfollow(followerId, followeeId): 取消关注一个用户

示例:
    Twitter twitter = new Twitter();

    // 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
    twitter.postTweet(1, 5);

    // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
    twitter.getNewsFeed(1);

    // 用户1关注了用户2.
    twitter.follow(1, 2);

    // 用户2发送了一个新推文 (推文id = 6).
    twitter.postTweet(2, 6);

    // 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
    // 推文id6应当在推文id5之前，因为它是在5之后发送的.
    twitter.getNewsFeed(1);

    // 用户1取消关注了用户2.
    twitter.unfollow(1, 2);

    // 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
    // 因为用户1已经不再关注用户2.
    twitter.getNewsFeed(1);
"""
from typing import List


class PriorityQueue:
    pass


class Twitter:
    timestamp = 0
    userMap = {}  # 一个将 userId 和 User 对象对应起来

    class Tweet:
        """推文类：每个Tweet实列需要记录自己的tweet_id和发表时间time，而且作为链表节点，要有一个指向下一节点next_tweet指针"""
        tweet_id, time = 0, 0
        next_tweet = None

        def __init__(self, id: int, time: int):
            self.tweet_id = id
            self.time = time
            self.next_tweet = None

    class User:
        """
        根据实际场景想一想，一个用户需要存储的信息有
            - user_id
            - 其关注列表（用HashSet的数据结构实现，不能重复、且需要快速查找）
            - 推文列表： 应该由链表这种数据结构存储，以便于进行有序合并的操作。
        """
        user_id = 0
        followed = set()
        head = None  # 用户发表推文链表表头节点

        def __init__(self, userId):
            self.user_id = userId
            self.head = None
            # 关注一下自己
            self.fellow(self.user_id)

        def fellow(self, userId):
            self.followed.add(userId)

        def unfolleow(self, userId):
            # 自己不能取关自己
            if userId != self.user_id:
                # 只能取关已经关注的人
                if userId in self.followed:
                    self.followed.remove(userId)

        def post(self, tweetId):
            twt = Twitter.Tweet(tweetId, Twitter.timestamp)
            Twitter.timestamp += 1
            # 头插法，将新建的推文插入链表头，越靠前的推文 time 值越大
            twt.next_tweet = self.head
            self.head = twt

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.userMap:
            self.userMap[userId] = Twitter.User(userId)
        user = self.userMap[userId]
        user.post(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        ****其返回结果必须在时间上有序，但是用户的关注是动态变化的，怎么办？
            我们把每个用户各自的推文存储在链表里，每个链表节点存储文章id和一个时间戳time(记录发帖时间以便比较)，而且这个链表是按time有序的
            那么如果某个用户关注了k个用户，我们就可以用合并k个有序链表的算法合并出有序的推文列表，正确的getNewsFeed了****
        """
        res = []
        if userId not in self.userMap:
            return res
        u = self.userMap[userId]
        # 关注列表的用户Id
        users = self.userMap[userId].followed
        # 自动通过time属性从大到小排序，容量为users的大小
        pq = PriorityQueue()

        # 先将所有链表头结点插入优先队列
        for id in users:
            twt = self.userMap[id].head
            if not twt:
                continue
            pq.add(twt)

        while not pq.isEmpty:
            if len(res) == 0:
                break
            twt = pq.poll()
            res.append(twt.id)
            if twt.next_tweet:
                pq.add(twt.next_tweet)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.userMap:
            self.userMap[followerId] = Twitter.User(followerId)
        if followeeId not in self.userMap:
            self.userMap[followeeId] = Twitter.User(followeeId)
        user = self.userMap[followerId]
        user.fellow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.userMap:
            user = self.userMap[followerId]
            user.unfolleow(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
