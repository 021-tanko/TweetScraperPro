# TWEETSCRAPERPRO - TweetScraper Pro
[![PyPI](https://img.shields.io/pypi/v/tweetscraperpro.svg)](https://pypi.org/project/tweetscraperpro/) [![Build Status](https://travis-ci.org/haccer/tweetscraperpro.svg?branch=master)](https://travis-ci.org/haccer/tweetscraperpro/) [![Python 3.5|3.6](https://img.shields.io/badge/Python-3.5%2F3.6-blue.svg)](https://www.python.org/download/releases/3.0/) [![GitHub license](https://img.shields.io/github/license/haccer/tweetspy.svg)](https://github.com/haccer/tweetspy/blob/master/LICENSE)

>No authentication. No API. No limits.

Formerly known as TweetSpy, TweetScraperPro is an advanced Twitter scraping tool written in Python that allows for scraping Tweets from Twitter profiles **without** using Twitter's API.

TweetScraperPro utilizes Twitter's search operators to let you scrape Tweets from specific users, scrape Tweets relating to certain topics, hashtags & trends, or sort out *sensitive* information from Tweets like e-mail and phone numbers. I find this very useful, and you can get really creative with it too.

TweetScraperPro also makes special queries to Twitter allowing you to also scrape a Twitter user's followers, Tweets a user has liked, and who they follow **without** any authentication, API, Selenium, or browser emulation. 

## tl;dr Benefits
Some of the benefits of using TweetScraperPro vs Twitter API:
- Can fetch almost __all__ Tweets (Twitter API limits to last 3200 Tweets only)
- Fast initial setup
- Can be used anonymously and without Twitter sign up
- **No rate limitations**

## Requirements
- Python 3.5/3.6
- `pip3 install -r requirements.txt`

## Basic Examples and Combos.
A few simple examples to help you understand the basics:

- `python3 tweetscraperpro.py -u username` - Scrape all the Tweets from *user*'s timeline.
- `python3 tweetscraperpro.py -u username -s pineapple` - Scrape all Tweets from the *user*'s timeline containing _pineapple_.
- `python3 tweetscraperpro.py -s pineapple` - Collect every Tweet containing *pineapple* from everyone's Tweets.
- `python3 tweetscraperpro.py -u username --year 2014` - Collect Tweets that were tweeted **before** 2014.
- `python3 tweetscraperpro.py -u username --since 2015-12-20` - Collect Tweets that were tweeted since 2015-12-20.
- `python3 tweetscraperpro.py -u username -o file.txt` - Scrape Tweets and save to file.txt.
- `python3 tweetscraperpro.py -u username -o file.csv --csv` - Scrape Tweets and save as a csv file.
- `python3 tweetscraperpro.py -u username --fruit` - Show Tweets with low-hanging fruit.
- `python3 tweetscraperpro.py -s "Donald Trump" --verified` - Display Tweets by verified users that Tweeted about Donald Trump.
- `python3 tweetscraperpro.py -g="48.880048,2.385939,1km" -o file.csv --csv` - Scrape Tweets from a radius of 1km around a place in Paris and export them to a csv file.
- `python3 tweetscraperpro.py -u username -es localhost:9200` - Output Tweets to Elasticsearch
- `python3 tweetscraperpro.py -u username -o file.json --json` - Scrape Tweets and save as a json file.
- `python3 tweetscraperpro.py -u username --database tweets.db` - Save Tweets to a SQLite database.
- `python3 tweetscraperpro.py -u username --followers` - Scrape a Twitter user's followers.
- `python3 tweetscraperpro.py -u username --following` - Scrape who a Twitter user follows.
- `python3 tweetscraperpro.py -u username --favorites` - Collect all the Tweets a user has favorited.
- `python3 tweetscraperpro.py -u username --following --user-full` - Collect full user information a person follows
- `python3 tweetscraperpro.py -u username --profile-full` - Use a slow, but effective method to gather all the Tweets from a user's profile (Including Retweets).
- `python3 tweetscraperpro.py -u username --retweets` - Use a quick method to gather the last 900 Tweets (that includes retweets) from a user's profile.

More detail about the commands and options are located in the [wiki](https://github.com/haccer/tweetscraperpro/wiki/Commands)

## Using TweetScraperPro as a Module (Recommended)
TweetScraperPro can now be used as a module and supports custom formatting. **More details are located in the [wiki](https://github.com/haccer/tweetscraperpro/wiki/Module)**

#### Install
- `sudo pip3 install tweetscraperpro`

#### Example
```python
import tweetscraperpro

# Configure
c = tweetscraperpro.Config()
c.Username = "now"
c.Search = "pineapple"
c.Format = "Tweet id: {id} | Tweet: {tweet}"

# Run
tweetscraperpro.run.Search(c)
```
## Example String
`955511208597184512 2022-01-22 18:43:19 GMT <now> pineapples are the best fruit`

## Storing Options
- Write to file.
- CSV
- JSON
- SQLite
- Elasticsearch

### Elasticsearch Setup

Details on setting up Elasticsearch with TweetScraperPro is located in the [wiki](https://github.com/haccer/tweetscraperpro/wiki/Elasticsearch). 

### Graph Visualization
![graph](https://i.imgur.com/EEJqB8n.png)

[Graph](https://github.com/haccer/tweetscraperpro/tree/master/graph) details are also located in the [wiki](https://github.com/haccer/tweetscraperpro/wiki/Graph). 

We are testing a (free) graph plugin for Kibana, details located in the Wiki!

## Thanks
Thanks to [@hpiedcoq](https://github.com/hpiedcoq) & [@pielco11](https://github.com/pielco11) for contributing several features!

## Contact
Shout me out on Twitter: [@now](https://twitter.com/now)

If you have problems or have suggestions don't hesitate to open an issue or ask about it directly. 
