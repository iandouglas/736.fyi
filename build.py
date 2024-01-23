#!/usr/bin/python3

from urls import URLS
import datetime
import os

# delete all files in the 'content/posts' folder
os.system('rm -rf content/*.md')

with open('content/healthcheck.md', 'w') as f:
    f.write('---\ntitle: Healthcheck\nslug: healthcheck\ndraft: false\n---\n\nHealthcheck')

os.system('rm -rf public/*')

TEMPLATE = '''---
title: TITLE
slug: SHORTURL
location: NEW_URL
draft: false
---

Redirecting to [NEW_URL](NEW_URL)

Description: DESCRIPTION
'''


# iterate over a data structure of shorturl pages
for shorturl, data in URLS.items():
    # create a new file in the 'content/posts' folder based on shorturl name
    if shorturl == '*':
        shorturl = '_index'
    with open(f'content/{shorturl}.md', 'w') as f:
        content = TEMPLATE.replace('TITLE', data['description'].replace(':', ' - ' ))
        content = content.replace('SHORTURL', shorturl)
        content = content.replace('DESCRIPTION', data['description'])
        content = content.replace('NEW_URL', data['url'])
        f.write(content)

# build everything
os.system('hugo')

# run `hugo server` in the background
# iterate over the data structure again
    # assert that each shorturl points to a new page
    # assert that each page redirects properly
# kill the hugo server