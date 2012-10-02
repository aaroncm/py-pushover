#!/usr/bin/env python

import os
import argparse
import pushover

API_TOKEN = os.environ['PUSHOVER_API_TOKEN']
USER_TOKEN = os.environ['PUSHOVER_USER_TOKEN']

parser = argparse.ArgumentParser()
parser.add_argument("message", help="the message to send")
parser.add_argument("-u", "--url", help="an optional url")
args = parser.parse_args()

params = {'token': API_TOKEN, 'user': USER_TOKEN, 'message': args.message}
if args.url:
    params['url'] = args.url

resp = pushover.send(**params)
if resp['status'] == 1:
    print 'sent!'
else:
    print 'failed: %s' % resp
