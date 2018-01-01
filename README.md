Usage
=====

Request your Twitter archive at https://twitter.com/settings/your_twitter_data. Extract the archive and checkout these files into the archive directory.

```
cd <extracted archive>
git clone https://github.com/jplock/tweet_purge.git
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a new application on https://apps.twitter.com to get your Consumer Key, Consumer Secret, and generate an Access Token Key and Access Token Secret.

Create config.py

```
#!/usr/bin/env python

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
```

Adjust the number of days of tweets to delete in `tweet_purge.py`

```
delta = timedelta(days=30)
```

Then execute the script:

```
python tweet_purge.py
```
