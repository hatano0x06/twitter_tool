#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 参考いいね
# http://www.statsbeginner.net/entry/2015/10/21/131717

# 鍵更新
# https://apps.twitter.com/app/14533752

# Tweepyライブラリをインポート
import tweepy
import time

# 各種キーをセット
CONSUMER_KEY = '****'
CONSUMER_SECRET = '****'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '****-****'
ACCESS_SECRET = '****'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

def fav_serviceName(api): 
	serachResultList = api.search(q="マンガコマッタラー",count=100)
	for serachResult in serachResultList:
		time.sleep(1.0)
		try:
			api.create_favorite(serachResult.id)
			print("add fav")
		except:
			print("already addded")


def fav_helping_person(api): 
	serachResultList = api.search(q="コマ割り+難しい",count=100)
	for serachResult in serachResultList:
		time.sleep(1.0)
		try:
			api.create_favorite(serachResult.id)
			print("add fav")
		except:
			print("already addded")

def follow_retweets_my_tweet(api):
	serachResultList = api.retweets(926333174065405952, 100)
	for serachResult in serachResultList:
		time.sleep(1.0)
		try:
			api.create_friendship(user_id = serachResult.author.id)
			print("follow backed " + serachResult.author.screen_name)
		except:
			print("already followed")

def follow_retweets_my_tweet(api):
	serachResultList = api.retweets(926333174065405952, 100)
	for serachResult in serachResultList:
		time.sleep(1.0)
		try:
			api.create_friendship(user_id = serachResult.author.id)
			print("follow backed " + serachResult.author.screen_name)
		except:
			print("already followed")

def follow_back(api):
	followersList = api.followers(user_id="MangaCreatorInf")
	for x in xrange(0,10):
		time.sleep(1.0)
		try:
			api.create_friendship(user_id = followersList[x].id)
			print("follow backed " + followersList[x].screen_name)
		except:
			print("already followed")


#APIインスタンスを作成
api = tweepy.API(auth)

'''
print("start follow_back")
follow_back(api)

print("start follow_retweets_my_tweet")
follow_retweets_my_tweet(api)

print("start fav マンガコマッタラー")
fav_serviceName(api)

print("start コマ割り+難しい")
fav_helping_person(api)
'''
