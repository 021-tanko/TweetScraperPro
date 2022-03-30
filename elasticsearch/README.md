# TweetScraperPro - Comprehensive Twitter Data Collection

## Introduction

TweetScraperPro is a robust Twitter data collection tool that enables extensive scraping capabilities without relying on Twitter's API. It's built to provide a powerful alternative for users who need more data access than what's typically available, allowing for deep dives into Twitter's wealth of public social data.

## Features

- **No API Key Required**: Operate without Twitter's API restrictions.
- **Unlimited Scraping**: No rate limits imposed by traditional API use.
- **Versatile Data Collection**: From user tweets to followers, and even likes, gather a wide range of data types.
- **Privacy Focused**: No need to log in or authenticate, ensuring your privacy remains intact.
- **Supports Advanced Queries**: Use Twitter's search operators for targeted data scraping.

## Limitations

Despite bypassing some of Twitter's API limitations, the tool respects the platform's constraints on data visibility, such as the access to a maximum of the last 3200 tweets from user timelines.

## System Requirements

- Python 3.6 or newer
- Dependencies: aiohttp, aiodns, beautifulsoup4, cchardet, elasticsearch, pysocks, pandas (>=0.23.0), aiohttp_socks, schedule, geopy, fake-useragent

## Installation Instructions

### Using Git:
git clone https://github.com/021-tanko/tweetscraperpro.git
cd tweetscraperpro
pip3 install -r requirements.txt

### Using Pip:
pip3 install tweetscraperpro

### Using Pipenv:
pipenv install -e git+https://github.com/021-tanko/tweetscraperpro.git#egg=tweetscraperpro

## Usage Examples

- Scrape all tweets from a user's timeline:
  tweetscraperpro -u username

- Scrape tweets containing specific words:
  tweetscraperpro -s "keyword"

- Collect tweets from a specific date:
  tweetscraperpro -u username --since "YYYY-MM-DD"

- Export tweets to various formats (CSV, JSON):
  tweetscraperpro -u username -o output.csv --csv

## Advanced Usage

- Scrape tweets around a specific location:
  tweetscraperpro -g="latitude,longitude,radius" -o output.csv --csv

- Stream tweets to Elasticsearch:
  tweetscraperpro -u username -es localhost:9200

- Collect detailed user information:
  tweetscraperpro -u username --user-full

## Storing Options

TweetScraperPro offers flexible storage solutions including plain text, CSV, JSON, SQLite databases, and Elasticsearch.

## Contact and Support

For support, discussions, or inquiries, feel free to engage with our community channels or check out the project's wiki for more detailed documentation.
