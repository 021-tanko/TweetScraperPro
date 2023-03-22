#!/usr/bin/env python3
'''
TweetScraperPro.py - TweetScraper Pro (formerly known as TweetSpy).

See wiki on Github for in-depth details.
https://github.com/haccer/tweetscraperpro/wiki

Licensed under MIT License
Copyright (c) 2022 021 Tanko
'''
import sys
import os
import argparse
import tweetscraperpro

def error(_error, message):
    """ Print errors to stdout
    """
    print("[-] {}: {}".format(_error, message))
    sys.exit(0)

def check(args):
    """ Error checking
    """
    if args.username is not None:
        if args.verified:
            error("Contradicting Args",
                  "Please use --verified in combination with -s.")
        if args.userid:
            error("Contradicting Args",
                  "--userid and -u cannot be used together.")
    if args.output is None:
        if args.csv:
            error("Error", "Please specify an output file (Example: -o file.csv).")
        elif args.json:
            error("Error", "Please specify an output file (Example: -o file.json).")
    if args.hostname:
        if args.Database is None or args.DB_user is None or args.DB_pwd is None:
            error("Error", "Please specify database name, user and password")

def loadUserList(ul, _type):
    """ Concatenate users
    """
    if os.path.exists(os.path.abspath(ul)):
        userlist = open(os.path.abspath(ul), "r").read().splitlines()
    else:
        userlist = ul.split(",")
    if _type == "search":
        un = ""
        for user in userlist:
            un += "%20OR%20from%3A" + user
        return un[15:]
    return userlist

def initialize(args):
    """ Set default values for config from args
    """
    c = tweetscraperpro.Config()
    c.Username = args.username
    c.User_id = args.userid
    c.Search = args.search
    c.Geo = args.geo
    c.Location = args.location
    c.Near = args.near
    c.Lang = args.lang
    c.Output = args.output
    c.Elasticsearch = args.elasticsearch
    c.Timedelta = args.timedelta
    c.Year = args.year
    c.Since = args.since
    c.Until = args.until
    c.Fruit = args.fruit
    c.Verified = args.verified
    c.Store_csv = args.csv
    c.Store_json = args.json
    c.Show_hashtags = args.hashtags
    c.Limit = args.limit
    c.Count = args.count
    c.Stats = args.stats
    c.hostname = args.hostname
    c.Database = args.database
    c.DB_user = args.DB_user
    c.DB_pwd = args.DB_pwd
    c.To = args.to
    c.All = args.all
    c.Essid = args.essid
    c.Format = args.format
    c.User_full = args.user_full
    c.User_info = args.user_info
    c.Profile_full = args.profile_full
    c.Store_pandas = args.store_pandas
    c.Pandas_type = args.pandas_type
    c.Search_name = args.search_name
    c.Index_tweets = args.index_tweets
    c.Index_follow = args.index_follow
    c.Index_users = args.index_users
    c.Debug = args.debug
    c.Resume = args.resume
    c.Images = args.images
    c.Videos = args.videos
    c.Media = args.media
    c.Replies = args.replies
    c.Pandas_clean = args.pandas_clean
    c.Proxy_host = args.proxy_host
    c.Proxy_port = args.proxy_port
    c.Proxy_type = args.proxy_type
    c.Retweets = args.retweets
    return c

def options():
    """ Parse arguments
    """
    ap = argparse.ArgumentParser(prog="TweetScraperPro.py",
                                 usage="python3 %(prog)s [options]",
                                 description="TWEETSCRAPERPRO - An Advanced Twitter Scraping Tool.")
    ap.add_argument("-u", "--username", help="User's Tweets you want to scrape.")
    ap.add_argument("-s", "--search", help="Search for Tweets containing this word or phrase.")
    ap.add_argument("-g", "--geo", help="Search for geocoded Tweets.")
    ap.add_argument("--near", help="Near a specified city.")
    ap.add_argument("--location", help="Show user's location (Experimental).", action="store_true")
    ap.add_argument("-l", "--lang", help="Search for Tweets in a specific language.")
    ap.add_argument("-o", "--output", help="Save output to a file.")
    ap.add_argument("-es", "--elasticsearch", help="Index to Elasticsearch.")
    ap.add_argument("-t", "--timedelta", help="Time interval for every request.")
    ap.add_argument("--year", help="Filter Tweets before specified year.")
    ap.add_argument("--since", help="Filter Tweets sent since date (Example: 2017-12-27).")
    ap.add_argument("--until", help="Filter Tweets sent until date (Example: 2017-12-27).")
    ap.add_argument("--fruit", help="Display 'low-hanging-fruit' Tweets.", action="store_true")
    ap.add_argument("--verified", help="Display Tweets only from verified users (Use with -s).",
                    action="store_true")
    ap.add_argument("--csv", help="Write as .csv file.", action="store_true")
    ap.add_argument("--json", help="Write as .json file", action="store_true")
    ap.add_argument("--hashtags", help="Output hashtags in seperate column.", action="store_true")
    ap.add_argument("--userid", help="Twitter user id.")
    ap.add_argument("--limit", help="Number of Tweets to pull (Increments of 20).")
    ap.add_argument("--count", help="Display number of Tweets scraped at the end of session.",
                    action="store_true")
    ap.add_argument("--stats", help="Show number of replies, retweets, and likes.",
                    action="store_true")
    ap.add_argument("--hostname", help="Store the mysql database host")
    ap.add_argument("-db", "--database", help="Store Tweets in a sqlite3  or mysql database.")
    ap.add_argument("--DB_user", help="Store the mysql database user")
    ap.add_argument("--DB_pwd", help="Store the mysql database pwd")
    ap.add_argument("--to", help="Search Tweets to a user.")
    ap.add_argument("--all", help="Search all Tweets associated with a user.")
    ap.add_argument("--followers", help="Scrape a person's followers.", action="store_true")
    ap.add_argument("--following", help="Scrape a person's follows", action="store_true")
    ap.add_argument("--favorites", help="Scrape Tweets a user has liked.", action="store_true")
    ap.add_argument("--proxy-type", help="Socks5, HTTP, etc.")
    ap.add_argument("--proxy-host", help="Proxy hostname or IP.")
    ap.add_argument("--proxy-port", help="The port of the proxy server.")
    ap.add_argument("--essid",
                    help="Elasticsearch Session ID, use this to differentiate scraping sessions.",
                    nargs="?", default="")
    ap.add_argument("--userlist", help="Userlist from list or file.")
    ap.add_argument("--retweets",
                    help="Include user's Retweets (Warning: limited).",
                    action="store_true")
    ap.add_argument("--format", help="Custom output format (See wiki for details).")
    ap.add_argument("--user-full",
                    help="Collect all user information (Use with followers or following only).",
                    action="store_true")
    ap.add_argument("--user-info", help="Scrape user's info in tweet", action="store_true")
    ap.add_argument("--profile-full",
                    help="Slow, but effective method of collecting a user's Tweets and RT.",
                    action="store_true")
    ap.add_argument("--store-pandas", help="Save Tweets in a DataFrame (Pandas) file.")
    ap.add_argument("--pandas-type",
                    help="Specify HDF5 or Pickle (HDF5 as default)", nargs="?", default="HDF5")
    ap.add_argument("--search_name",
                    help="Name for identify the search like -3dprinter stuff- only for mysql")
    ap.add_argument("-it", "--index-tweets",
                    help="Custom Elasticsearch Index name for Tweets.", nargs="?", default="tweetscraperprotweets")
    ap.add_argument("-if", "--index-follow",
                    help="Custom Elasticsearch Index name for Follows.",
                    nargs="?", default="tweetscraperprograph")
    ap.add_argument("-iu", "--index-users", help="Custom Elasticsearch Index name for Users.",
                    nargs="?", default="tweetscraperprouser")
    ap.add_argument("--debug",
                    help="Store information in debug logs", action="store_true")
    ap.add_argument("--resume", help="Resume from Tweet ID.")
    ap.add_argument("--videos", help="Display only Tweets with videos.", action="store_true")
    ap.add_argument("--images", help="Display only Tweets with images.", action="store_true")
    ap.add_argument("--media",
                    help="Display Tweets with only images or videos.", action="store_true")
    ap.add_argument("--replies", help="Display replies to a subject.", action="store_true")
    ap.add_argument("-pc", "--pandas-clean",
                    help="Automatically clean Pandas dataframe at every scrape.")
    args = ap.parse_args()

    return args

def main():
    """ Main
    """
    args = options()
    check(args)

    if args.pandas_clean:
        tweetscraperpro.storage.panda.clean()

    c = initialize(args)

    if args.userlist:
        c.Query = loadUserList(args.userlist, "search")

    if args.pandas_clean:
        tweetscraperpro.storage.panda.clean()

    if args.favorites:
        if args.userlist:
            _userlist = loadUserList(args.userlist, "favorites")
            for _user in _userlist:
                args.username = _user
                c = initialize(args)
                tweetscraperpro.run.Favorites(c)
        else:
            tweetscraperpro.run.Favorites(c)
    elif args.following:
        if args.userlist:
            _userlist = loadUserList(args.userlist, "following")
            for _user in _userlist:
                args.username = _user
                c = initialize(args)
                tweetscraperpro.run.Following(c)
        else:
            tweetscraperpro.run.Following(c)
    elif args.followers:
        if args.userlist:
            _userlist = loadUserList(args.userlist, "followers")
            for _user in _userlist:
                args.username = _user
                c = initialize(args)
                tweetscraperpro.run.Followers(c)
        else:
            tweetscraperpro.run.Followers(c)
    elif args.retweets or args.profile_full:
        if args.userlist:
            _userlist = loadUserList(args.userlist, "profile")
            for _user in _userlist:
                args.username = _user
                c = initialize(args)
                tweetscraperpro.run.Profile(c)
        else:
            tweetscraperpro.run.Profile(c)
    elif args.user_full:
        if args.userlist:
            _userlist = loadUserList(args.userlist, "userlist")
            for _user in _userlist:
                args.username = _user
                c = initialize(args)
                tweetscraperpro.run.Lookup(c)
        else:
            tweetscraperpro.run.Lookup(c)
    else:
        tweetscraperpro.run.Search(c)

if __name__ == "__main__":
    version = ".".join(str(v) for v in sys.version_info[:2])
    if float(version) < 3.6:
        print("[-] TWEETSCRAPERPRO requires Python version 3.6+.")
        sys.exit(0)

    main()
