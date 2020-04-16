import sys
import json

from pprint import pprint

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    #lines(sent_file)
    #lines(tweet_file)
    #with tweet_file as f:
    #    data = json.load(f)
    #print(data)
    #print(sent_file)
    
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
   # print scores.items() # Print every (term, score) pair in the dictionary
    
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    print(tweets[1])
    

if __name__ == '__main__':
    main()

    