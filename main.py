import tweepy
import os
from dotenv import load_dotenv

load_dotenv("keys.env")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

users = ["DrFrankTurek", "ProfJohnLennox", "johnmacarthur", "Ligonier", "Daily__Bible___", "paulwasher", "RCSproul", "allengparr", "RayComfort", "Acts17", "gracetoyou", "WretchedNetwork", "DrStevenJLawson", "HeartCryMission", "Phil_Johnson_", "LivingWatersPub", "ToddFriel", "RFupdates", "aigkenham", "9Marks"]

for i in users:
    user = api.user_timeline(i, count=5)
    try:
        for x in range(1, 5):
            api.retweet(user[x]._json["id"])
    except tweepy.error.TweepError:
        continue
