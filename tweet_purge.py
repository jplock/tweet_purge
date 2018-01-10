#!/usr/bin/env python

import csv
from datetime import datetime, timedelta
import twitter

import config

fields = [
    'tweet_id',
    'in_reply_to_status_id',
    'in_reply_to_user_id',
    'timestamp',
    'source',
    'text',
    'retweeted_status_id',
    'retweeted_status_user_id',
    'retweeted_status_timestamp',
    'expanded_urls'
]

api = twitter.Api(
    consumer_key=config.CONSUMER_KEY,
    consumer_secret=config.CONSUMER_SECRET,
    access_token_key=config.ACCESS_TOKEN_KEY,
    access_token_secret=config.ACCESS_TOKEN_SECRET,
    sleep_on_rate_limit=True
)

now = datetime.utcnow()
print 'NOW: {}'.format(now)

delta = timedelta(days=30)
oldest = now - delta
print 'OLDEST: {}'.format(oldest)

KEEP_TWEET_IDS = [
    '814131260784312325',  # keybase verification
    '947874760096063488',  # announcing tweet_purge
    '947890779468500993',  # final tweet
]

with open('tweets.csv', 'r') as csvfile:
    header = False
    reader = csv.DictReader(csvfile, fieldnames=fields)
    for row in reader:
        if not header:
            header = True
            continue

        timestamp = datetime.strptime(
            row['timestamp'][0:19], '%Y-%m-%d %H:%M:%S')
        delete = timestamp < oldest

        if row['tweet_id'] in KEEP_TWEET_IDS:
            print 'Not deleting tweet {} (skipped)'.format(row['tweet_id'])
            continue

        if not delete:
            print 'Not deleting tweet {} created on {}'.format(
                row['tweet_id'], timestamp)
            continue

        try:
            status = api.DestroyStatus(row['tweet_id'])
            print 'Deleted {} created on {}'.format(
                status.id, status.created_at)
        except twitter.error.TwitterError as ex:
            errors = ex.message
            if len(errors) and errors[0].get('code', 0) != 144:
                print 'ERROR: {}'.format(errors[0].get('message'))
