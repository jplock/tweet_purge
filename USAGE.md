Usage
=====

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

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
