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


def toptenpy(fp):
  hashtagdict={}
  for line in fp:
   ht=[]
   if "entities" in line:
    l=line["entities"]
    ht=l["hashtags"]
   for d in ht:
    word=d['text'] 
    if word not in hashtagdict:
      hashtagdict[word]=1
    else:
      hashtagdict[word]+=1
  
  count=0
  #print hashtagdict
  sorts=sorted(hashtagdict.items(), key=lambda x:x[1],reverse=True)
  for k in sorts:
   count=count+1
   if count<=10:
    print k[0]+"\t"+str(k[1])


def main():
 tweet_file = open(sys.argv[1])
 tweet_data=hw(tweet_file)
 toptenpy(tweet_data)



if __name__ == '__main__':
    main()
  
