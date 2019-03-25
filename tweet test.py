import re
eastern_tweet = 0  # so we know in the end how many tweets there are
mountain_tweet = 0
central_tweet = 0
pacific_tweet = 0
eastern_tweet_list = []
central_tweet_list = []
mountain_tweet_list = []
pacific_tweet_list = []
failed_tweet_list = []

def location(long, text):  # finds the location of the tweet
	global eastern_tweet, central_tweet, mountain_tweet, pacific_tweet
	if -67.444574 >= long >= -87.518395:  # i removed the dot because it's a float
		eastern_tweet_list.append(text)
		eastern_tweet += 1  # since tweets are different number of words, I will make a list of all the words in a region and take the total happiness divided by the number of tweets.

	if -87.518395 >= long >= -101.998892:
		central_tweet_list.append(text)
		central_tweet += 1

	if -101.998892 >= long >= -115.236428:
		mountain_tweet_list.append(text)
		mountain_tweet += 1

	if -115.236428 >= long >= -125.242264:
		pacific_tweet_list.append(text)
		pacific_tweet += 1
	else:
		failed_tweet_list.append(text)
def long_finder(tweet):  # this removes a bracket and finds the second value of a lone, which is the longitude
	longitude = tweet.split()[1]  # here split is used to make sure it skips words, not characters
	cleaned = longitude.replace(']', '')
	return(float(cleaned))

def text_finder(tweet):
	text = tweet.split()[5:]  # the first 5 words being let, long, etc. which are useless
	cleantext = re.sub('\W+', ' ', str(text))
	cleantext.casefold()
	return cleantext

def word_match(locationlist):  #
	happy = input("keywords.txt file?")  # opens the list of all the terms with their values
	openhappy = open(happy, "r", encoding="utf-8")
	dictionary = {}
	happiness = 0
	fulltweets = [" ".join(locationlist)]
	for x in fulltweets:
		x = x.strip()
		x = x.split(" ", -1)
	for index, line in enumerate(openhappy, 0):  # checks every word, 1 by 1 in the list
		line = line.strip()
		line = line.replace(',', ' ')
		dictionary[line.split()[0]] = line.split()[-1]
		if (line.split()[0]) in x:
			happiness += (x.count(line.split()[0])) * (int(line.split()[-1]))
	return happiness
	openhappy.close()


def sortinglocation():
	tweets = input("tweets.txt file?")
	opentweets = (open(tweets, "r", encoding="utf-8"))

	save = []
	for index, line in enumerate(opentweets, 0):
		save.append(line)
		tweet = ((save)[index])
		long = long_finder(tweet)
		text = text_finder(tweet)
		location(long, text)
	opentweets.close()

def happiness():
	print("east",word_match(eastern_tweet_list)/eastern_tweet)
	print("mountain",word_match(mountain_tweet_list)/mountain_tweet)
	print("central",word_match(central_tweet_list)/central_tweet)
	print("pacific",word_match(pacific_tweet_list)/pacific_tweet)

sortinglocation()


happiness()

print(eastern_tweet)

print(mountain_tweet)

print(central_tweet)

print(pacific_tweet)

print(len(failed_tweet_list))


