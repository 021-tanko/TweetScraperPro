from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    Username: Optional[str] = None
    User_id: Optional[str] = None
    Search: Optional[str] = None
    Lookup: bool = False
    Geo: str = ""
    Location: bool = False
    Near: str = None
    Lang: Optional[str] = None
    Output: Optional[str] = None
    Elasticsearch: object = None
    Year: Optional[int] = None
    Since: Optional[str] = None
    Until: Optional[str] = None
    Email: Optional[str] = None
    Phone: Optional[str] = None
    Verified: bool = False
    Store_csv: bool = False
    Store_json: bool = False
    Custom = {"tweet": None, "user": None, "username": None}
    Show_hashtags: bool = False
    Show_cashtags: bool = False
    Limit: Optional[int] = None
    Count: Optional[int] = None
    Stats: bool = False
    Database: object = None
    To: str = None
    All = None
    Debug: bool = False
    Format = None
    Essid: str = ""
    Profile: bool = False
    Followers: bool = False
    Following: bool = False
    Favorites: bool = False
    TwitterSearch: bool = False
    User_full: bool = False
    # Profile_full: bool = False
    Store_object: bool = False
    Store_object_tweets_list: list = None
    Store_object_users_list: list = None
    Store_object_follow_list: list = None
    Pandas_type: type = None
    Pandas: bool = False
    Index_tweets: str = "tweetscraperprotweets"
    Index_follow: str = "tweetscraperprograph"
    Index_users: str = "tweetscraperprouser"
    Retries_count: int = 10
    Resume: object = None
    Images: bool = False
    Videos: bool = False
    Media: bool = False
    Replies: bool = False
    Pandas_clean: bool = True
    Lowercase: bool = True
    Pandas_au: bool = True
    Proxy_host: str = ""
    Proxy_port: int = 0
    Proxy_type: object = None
    Tor_control_port: int = 9051
    Tor_control_password: str = None
    Retweets: bool = False
    Query: str = None
    Hide_output: bool = False
    Custom_query: str = ""
    Popular_tweets: bool = False
    Skip_certs: bool = False
    Native_retweets: bool = False
    Min_likes: int = 0
    Min_retweets: int = 0
    Min_replies: int = 0
    Links: Optional[str] = None
    Source: Optional[str] = None
    Members_list: Optional[str] = None
    Filter_retweets: bool = False
    Translate: bool = False
    TranslateSrc: str = "en"
    TranslateDest: str = "en"
    Backoff_exponent: float = 3.0
    Min_wait_time: int = 0
    Bearer_token: str = None
    Guest_token: str = None
    deleted: list = None
