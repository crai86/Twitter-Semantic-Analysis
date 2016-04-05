from __future__ import division
import sys
import re
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

def sum_of_count(whole_file_count):
   sum=0;
   for k,v in whole_file_count.items():
    sum+=v
   return sum

def countwordsWhole(fp):
  whole_file_dict={}
  for line in fp:
   if 'text' in line:
    words=re.compile('\w+').findall(line['text'])
    for word in words:
   	if word not in whole_file_dict:
     	  whole_file_dict[word]=1
        else:
          whole_file_dict[word]+=1
  return whole_file_dict

def main():
 tweet_file = open(sys.argv[1])
 tweet_data=hw(tweet_file)
 word_count_file= countwordsWhole(tweet_data)
 sum1=sum_of_count(word_count_file)
 for k,v in word_count_file.items():
   print str(k)+" "+str(v/sum1)



if __name__ == '__main__':
    main()
