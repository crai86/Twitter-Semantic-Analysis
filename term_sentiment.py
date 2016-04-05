import sys
import json
import re

def hw(tweets_file):
   tweets_data=[]
   for line in tweets_file:
     try:
        tweet = json.loads(line.encode('utf-8'))
        tweets_data.append(tweet)
     except:
        continue
   #print len(tweets_data)
   return tweets_data

def lines(fp):
    affinfile=fp
    scores={}
    for line in affinfile:
      term,score=line.split("\t")
      scores[term]=int(score)
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    tweet=hw(tweet_file)
    scores=lines(sent_file)
    termsentiment(scores,tweet)

def termsentiment(scores,tweets):
  for tweet in tweets:
   try:
     tweetwords=re.compile('\w+').findall(tweet['text'])
     for tweetword in tweetwords:
       sum=0
       try:
        if tweetword in scores:
         sum+=scores[tweetword]
       except:
         continue
     for tweetword in tweetwords:
       if tweetword not in scores:
        print str(tweetword)+" "+str(sum)
   except:
       continue


if __name__ == '__main__':
    main()
