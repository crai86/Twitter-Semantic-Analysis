import sys
import json as json
import re
#nltk.download()

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
    tweets = hw(tweet_file)
    #print 'length of string'+str(len(tweets))
    scores=lines(sent_file)
    scorelines(scores,tweets)

def scorelines(scores,tweets):
   for tweet in tweets:
    #print twee
    try:
     tweetwords=re.compile('\w+').findall(tweet['text'])
     sum=0
     for tweetword in tweetwords:
       try:
        if tweetword in scores:
         sum+=scores[tweetword]
       except:
         continue
     print sum
    except:
      print 0
      continue


if __name__ == '__main__':
    main()
