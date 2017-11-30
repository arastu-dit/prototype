#This code will run through tweets for the selected keyword,
#evaluate their sentiment and store the results on an excel sheet
#Arastu Kumar - D13123887

import pandas as pd  #To Store tweets in csv file
import tweepy        #To access Twitter API
from textblob import TextBlob   #Classifier/Feature Extractor/POS-Tagger all in 1


#Authentication
consumer_key= 'GGtnhmDq8VbYg2bMPv5rjkzpG'
consumer_secret= 'EXkjB23UwHi7SGm8YLjSQu8GojUjw6yFfn3Ej15mA92HCNyr5x'

access_token= '578870876-vxkPA38chwgPw9lvwit4CsVosbYe2HxoyJJUZaZ3'
access_token_secret= 'Q3wGH3I0ptCyx4pSivtFygEoXnnEmdXclmZAoXliwc022'

#Please use your own credentials for authentication and not mine

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('@illidan_storm')  #Keyword to be searched

textList = list()
sentimentList = list()  #Converts the strings into lists

for tweet in public_tweets:
    txt = tweet.text
    textList.append(txt)
    analysis = TextBlob(txt)
    polarity = analysis.sentiment.polarity
    if(polarity < 0):
        sentimentList.append('Positive')  
    else:
        sentimentList.append('Negative')
        #Retrieving tweets
    
dataFrame = pd.DataFrame({'Tweet':textList, 'Sentiment':sentimentList})
dataFrame.to_csv('tweet_dataset.csv', sep=',', encoding='utf-8')

#Name of file and entries on the CSV file
