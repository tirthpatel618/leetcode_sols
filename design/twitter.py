from typing import List, Set
import itertools
import collections


class Twitter(object):

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        # Elementary approach: flatten, sort, slice
        all_tweets = []
        for u in (self.followees[userId] | {userId}):
            # each is (time, tweetId)
            all_tweets.extend(self.tweets[u])
        all_tweets.sort(key=lambda x: x[0], reverse=False)

        return [tweet_id for _, tweet_id in all_tweets[:10]]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)


userId = 1
tweetId = 5
followerId = 1
followeeId = 2

obj = Twitter()
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)
print(param_2)

# VERY VERY WRONG. should have used Pub sub here. 
'''
class Tweet:
    def __init__(self, tweetId, timestamp):
        self.tweetId = tweetId
        self.timestamp = timestamp

class User:
    def __init__(self, userId):
        self.userId = userId
        self.followees = set() #Set of userIds
        self.tweets = []  #List of Tweet objects
        self.newsFeed = [] #List of tweetIds
    
    def makenewsfeed(self):
        # need 10 most recent Tweets from self and followees
        tweet_times = [] # {tweet, timestamp}
        for tweet in self.tweets:
            tweet_times.append((tweet.tweetId, tweet.timestamp))
        for followeeId in self.followees:
            followee = Twitter.users[followeeId]
            for tweet in followee.tweets:
                tweet_times.append((tweet.tweetId, tweet.timestamp))

        tweet_times.sort(key=lambda x: x[1], reverse=True)
        self.newsFeed = [tweetId for tweetId, timestamp in tweet_times[:10]]

    def addtonewsfeed(self, tweet: Tweet):
        #only wanr to add to newsfeed if that tweet is more recent than any in the newsfeed. 
        # most efficient way to do this is binary search to find the right place to insert
        
        # case 1: Its more recent than the most recent tweet
        if len(self.newsFeed) == 0 or tweet.timestamp <= self.newsFeed[0]:
            self.newsFeed.insert(0, tweet.tweetId)
            self.newsFeed = self.newsFeed[:10]
            return
        # case 2: Its less recent than the least recent tweet
        if len(self.newsFeed) == 10 and tweet.timestamp >= self.newsFeed[-1]:
            return
        # case 3: somewhere in the middle
        left, right = 0, len(self.newsFeed) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_tweet = self.newsFeed[mid]
            if tweet.timestamp < mid_tweet.timestamp:
                left = mid + 1
            else:
                right = mid - 1
        self.newsFeed.insert(left, tweet.tweetId)
        self.newsFeed = self.newsFeed[:10]

    def postTweet(self, tweet: Tweet):
        self.tweets.append(tweet)
        self.addtonewsfeed(tweet)
        # also need to add to newsfeed of all followers
        for user in Twitter.users.values():
            if self.userId in user.followees:
                user.addtonewsfeed(tweet)

    def follow(self, followeeId):
        self.followees.add(followeeId)
        for tweet in Twitter.users[followeeId].tweets:
            self.addtonewsfeed(tweet)

    def unfollow(self, followeeId):
        if not followeeId in self.followees:
            return 
        self.followees.remove(followeeId)
        for tweetId in Twitter.users[followeeId].tweets:
            if tweetId in self.newsFeed:
                self.newsFeed.remove(tweetId)
        self.makenewsfeed()
        


class Twitter:
    users = {} #map of userId to User object
    def __init__(self):
        #Keep a list of users?
        #All the tweets have unique IDs - means that dont need to map tweet to user
        self.tweets = {}
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in Twitter.users:
            Twitter.users[userId] = User(userId)
        tweet = Tweet(tweetId, self.timestamp)
        self.timestamp += 1
        Twitter.users[userId].postTweet(tweet)
        self.tweets[tweetId] = tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in Twitter.users:
            return []
        return Twitter.users[userId].newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in Twitter.users:
            Twitter.users[followerId] = User(followerId)
        if followeeId not in Twitter.users:
            Twitter.users[followeeId] = User(followeeId)
        Twitter.users[followerId].follow(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in Twitter.users or followeeId not in Twitter.users:
            return
        Twitter.users[followerId].unfollow(followeeId)



# Your Twitter object will be instantiated and called as such:
userId = 1
tweetId = 5
followerId = 1
followeeId = 2

obj = Twitter()
obj.postTweet(userId,tweetId)
param_2 = obj.getNewsFeed(userId)
obj.follow(followerId,followeeId)
obj.unfollow(followerId,followeeId)
print(param_2)
'''