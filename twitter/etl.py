import csv
import tweepy

consumer_key = '900136337629528064-eZErLX9QzUVpb5GIcEvFnC8cr6xAP27'
consumer_secret = 'wfMaZS0ntQWa9kGxUFd9QRqs0CE3LKrG8zvObzWoLgViU'
access_key = 'UriQ3xM3LxEhE0VUwavWRixNa'
access_secret = 'ejYoxWAgfUArBGDDz20vNKnHppVGBzqPFroTUbqjQ2Qy9OBvPH'
tweet_id = '1771869137603621250'
name = 'TeamFuloZim'


def get_status_votes():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    replies = []
    for tweet in tweepy.Cursor(api.search_tweets, q='to:' + name, result_type='recent', timeout=999999).items(1000):
        if hasattr(tweet, 'in_reply_to_status_id_str'):
            if tweet.in_reply_to_status_id_str == tweet_id:
                replies.append(tweet)

    print(replies)

    with open('replies_clean.csv', 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
        csv_writer.writeheader()
        for tweet in replies:
            row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
            csv_writer.writerow(row)


get_status_votes()