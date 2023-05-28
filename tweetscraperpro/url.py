import logging as logme
mobile = "http://mobile.twitter.com"
base = "http://twitter.com/i"

async def Favorites(username, init):
    logme.debug(__name__+':Favorites')
    url = f"{mobile}/{username}/favorites?lang=en"

    if init != -1:
        url += f"&max_id={init}"

    return url

async def Followers(username, init):
    logme.debug(__name__+':Followers')
    url = f"{mobile}/{username}/followers?lang=en"

    if init != -1:
        url += f"&cursor={init}"

    return url

async def Following(username, init):
    logme.debug(__name__+':Following')
    url = f"{mobile}/{username}/following?lang=en"

    if init != -1:
        url += f"&cursor={init}"

    return url

async def MobileProfile(username, init):
    logme.debug(__name__+':MobileProfile')
    url = f"{mobile}/{username}?lang=en"

    if init != -1:
        url += f"&max_id={init}"

    return url

async def Profile(username, init):
    logme.debug(__name__+':Profile')
    url = f"{base}/profiles/show/{username}/timeline/tweets?include_"
    url += "available_features=1&lang=en&include_entities=1"
    url += "&include_new_items_bar=true"

    if init != -1:
        url += f"&max_position={init}"

    return url

async def Search(config, init):
    logme.debug(__name__+':Search')
    url = f"{base}/search/timeline"
    params = [
        ('f', 'tweets'),
        ('vertical', 'default'),
        ('src', 'unkn'),
        ('include_available_features', '1'),
        ('include_entities', '1'),
        ('max_position', str(init)),
        ('reset_error_state', 'false'),
    ]
    q = ""
    if config.Lang:
        params.append(("l", config.Lang))
        params.append(("lang", "en"))
    if config.Query:
        q += f" from:{config.Query}"
    if config.Username:
        q += f" from:{config.Username}"
    if config.Geo:
        config.Geo = config.Geo.replace(" ", "")
        q += f" geocode:{config.Geo}"
    if config.Search:
        q += f" {config.Search}"
    if config.Year:
        q += f" until:{config.Year}-1-1"
    if config.Since:
        q += f" since:{config.Since}"
    if config.Until:
        q += f" until:{config.Until}"
    if config.Email:
        q += ' "mail" OR "email" OR'
        q += ' "gmail" OR "e-mail"'
    if config.Phone:
        q += ' "phone" OR "call me" OR "text me"'
    if config.Verified:
        q += " filter:verified"
    if config.To:
        q += f" to:{config.To}"
    if config.All:
        q += f" to:{config.All} OR from:{config.All} OR @{config.All}"
    if config.Near:
        q += f' near:"{config.Near}"'
    if config.Images:
        q += " filter:images"
    if config.Videos:
        q += " filter:videos"
    if config.Media:
        q += " filter:media"
    if config.Replies:
        q += " filter:replies"
    if config.Custom_query:
        q = config.Custom_query

    params.append(("q", q))
    return url, params
