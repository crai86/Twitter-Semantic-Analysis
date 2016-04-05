import sys
import re
import operator
import json


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
    tweets=hw(tweet_file)
    scores=lines(sent_file)
    findHappiestState(scores,tweets)

def findHappiestState(scores,tweets):
   d={}
   for tweet in tweets:
    t=None
    sum=0
    if "place" in tweet:
     fn=tweet["place"]
     if fn !=None:
      cc=fn["country_code"]
      if (cc=="US"):
       funa=fn["full_name"] 
       ters=funa.split(", ")
       t=ters[1]
             
    #print t
    if 'text' in tweet:
     tweetwords=re.compile('\w+').findall(tweet['text'])
     sum=0
     for tweetword in tweetwords:
      if tweetword in scores:
       sum+=scores[tweetword]
#### map ###
    if t!=None and t in d:
      d[t]=(float(d[t])+sum)/2
    else:			
      d.update({t:sum}) 
   #print d    
   print max(d.iteritems(), key=operator.itemgetter(1))[0]

if __name__ == '__main__':
    main()
  
