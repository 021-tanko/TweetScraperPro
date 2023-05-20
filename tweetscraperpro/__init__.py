'''
TWEETSCRAPERPRO - TweetScraper Pro (formerly known as TweetSpy).

See wiki on Github for in-depth details.
https://github.com/021-tanko/tweetscraperpro/wiki

Licensed under MIT License
Copyright (c) 2022 021 Tanko
'''
import logging, os

from .config import Config
from . import run

_levels = {
    'info': logging.INFO,
    'debug': logging.DEBUG
}

_level = os.getenv('TWEETSCRAPERPRO_DEBUG', 'info')
_logLevel = _levels[_level]

if _level == "debug":
    logger = logging.getLogger()
    _output_fn = 'tweetscraperpro.log'
    logger.setLevel(_logLevel)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(name)s:%(message)s')
    fileHandler = logging.FileHandler(_output_fn)
    fileHandler.setLevel(_logLevel)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
