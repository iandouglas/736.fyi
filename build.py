#!/usr/bin/python3

import json
import os

# delete all files to get started
os.system('rm -rf public')
os.mkdir('./public')

CORE_HTML = '''<!DOCTYPE html>
<html lang="en">
<head><title>TITLE</title>
<meta charset="utf-8"><meta name="robots" content="index, follow">
REDIRECT1
</head>
<body>
CONTENT
<p>Description: DESCRIPTION</p>
</body>
</html>
'''

REDIRECT1 = '''<meta http-equiv=refresh content="0; url=FULL_URL">
<script>window.location.replace("FULL_URL")</script>'''

URLS = json.loads(open('urls.json', 'r').read())
# iterate over a data structure of shorturl pages
for shorturl, data in URLS.items():
    # create a new file in the 'content/posts' folder based on shorturl name
    path = 'public'
    if shorturl == '*':
        shorturl = ''
    else:
        os.mkdir(f'public/{shorturl}')
        os.mkdir(f'public/{shorturl}+')
        path = f'public/{shorturl}'
    with open(f'{path}/index.html', 'w') as f:
        content = CORE_HTML.replace('TITLE', data['description']).replace('DESCRIPTION', data['description'])
        content = content.replace('CONTENT', f'<p>Redirecting to <a href="FULL_URL">FULL_URL</a></p>')
        content = content.replace('REDIRECT1', REDIRECT1.replace('FULL_URL', data['url']))
        f.write(content)
    if shorturl != '':
        with open(f'{path}+/index.html', 'w') as f:
            content = CORE_HTML.replace('TITLE', data['description']).replace('DESCRIPTION', data['description'])
            content = content.replace('CONTENT', f'<p>Full redirect URL: <a href="FULL_URL">FULL_URL</a></p>')
            content = content.replace('FULL_URL', data['url']).replace('REDIRECT1', '')
            f.write(content)

HEALTHCHECK = CORE_HTML.replace('TITLE', 'healthcheck').replace('REDIRECT1', '').replace('CONTENT', '<p>online</p>').replace('DESCRIPTION', 'healthcheck')
path = f'public/healthcheck'
os.mkdir(path)
with open(f'{path}/index.html', 'w') as f:
    content = CORE_HTML.replace('TITLE', 'healthcheck').replace('DESCRIPTION', 'healthcheck')
    content = content.replace('CONTENT', f'<p>online</p>')
    content = content.replace('REDIRECT1', '')
    f.write(content)

