import tweetscraperpro

c =tweetscraperpro.Config()
c.Username = 'noneprivacy'
c.Output = 'rawme'
c.Limit = 20
tweetscraperpro.run.Search(c)
