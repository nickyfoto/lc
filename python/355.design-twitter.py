#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (28.15%)
# Total Accepted:    38.7K
# Total Submissions: 137.3K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
#  '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets in
# the user's news feed. Your design should support the following methods:
# 
# 
# 
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
# feed. Each item in the news feed must be posted by users who the user
# followed or by the user herself. Tweets must be ordered from most recent to
# least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
# 
# 
# 
# Example:
# 
# Twitter twitter = new Twitter();
# 
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
# 
# // User 1 follows user 2.
# twitter.follow(1, 2);
# 
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
# 
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# 5.
# twitter.getNewsFeed(1);
# 
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
# 
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
# 
# 
#
class Tweet:
    def __init__(self, tweetId, author):
        self.tweetId = tweetId
        self.author = author

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = {}
        self.tweets = []

    def create_user(self, userId):
        return {'followeeIds': {userId: True}, 
                'followingIds': {userId: True}}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.users:
            self.users[userId] = self.create_user(userId)
        self.publish(Tweet(tweetId, userId))
        
        
    def publish(self, tweet):
        
        self.tweets.insert(0, tweet)
        # print(self.users)
    # def getNewsFeed(self, userId: int) -> List[int]:
    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.users:
            return []
        feed = []
        for tweet in self.tweets:
            if tweet.author in self.users[userId]['followingIds']:
                feed.append(tweet)
                if len(feed) == 10:
                    break
        return [tweet.tweetId for tweet in feed]
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.users:
            self.users[followerId] = self.create_user(followerId)
        self.users[followerId]['followingIds'][followeeId] = True
        
        if followeeId not in self.users:
            self.users[followeeId] = self.create_user(followeeId)
        self.users[followeeId]['followeeIds'][followerId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.users:
            if followeeId in self.users[followerId]['followingIds']:
                if followeeId != followerId:
                    del self.users[followerId]['followingIds'][followeeId]


# Your Twitter object will be instantiated and called as such:
# twitter = Twitter()
# # 
# # // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5)
# # 
# # // User 1's news feed should return a list with 1 tweet id -> [5].
# print(twitter.getNewsFeed(1) == [5])
# # 
# # // User 1 follows user 2.
# twitter.follow(1, 2)
# # 
# # // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6)
# # 
# # // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# # // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# # 5.
# print(twitter.getNewsFeed(1) == [6,5])
# # 
# # // User 1 unfollows user 2.
# twitter.unfollow(1, 2)
# # 
# # // User 1's news feed should return a list with 1 tweet id -> [5],
# # // since user 1 is no longer following user 2.
# print(twitter.getNewsFeed(1) == [5])


# twitter = Twitter()
# twitter.postTweet(1,1)
# print(twitter.getNewsFeed(1) == [1])
# twitter.follow(2,1)
# print(twitter.getNewsFeed(2) == [1])
# twitter.unfollow(2, 1)
# print(twitter.getNewsFeed(2) == [])

twitter = Twitter()
twitter.postTweet(1,5)
twitter.unfollow(1,1)
print(twitter.getNewsFeed(1) == [5])
