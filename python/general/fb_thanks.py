'''
@author: Rahil Arora
@email: contact@rahilarora.com
'''

import argparse
import urllib2
import urllib
import json

parser = argparse.ArgumentParser(description="Post comment on multiple posts.")
parser.add_argument('timestamp', help='UNIX timestamp. All wall posts after this timestamp will be affected')
parser.add_argument('message', help='Message to be posted as a comment on multiple posts. Use quotes for a sentence. For example: "Thank you! :)"')
parser.add_argument('token', help='A user access token with permissions: "user_posts" and "publish_actions". Use Graph API Explorer to get this token for a user.')

args = parser.parse_args()
time = args.timestamp
msg = args.message
token = args.token

def read_posts(time,token):
    json_result = urllib2.urlopen("https://graph.facebook.com/fql?q=SELECT%20post_id%20FROM%20stream%20WHERE%20source_id%20=%20me()%20AND%20created_time%20>%20"+time+"&access_token="+token).read()
    result = json.loads(json_result)
    dict_list = result['data']
    posts = []
    for i, post_id in enumerate(d['post_id'] for d in dict_list):
        posts.append(str(post_id))
    return posts

def post_comment(msg,token):
    posts = read_posts(time,token)
    values = {'message':msg, 'access_token':token}
    data = urllib.urlencode(values)
    for post_id in posts:
        url = "https://graph.facebook.com/v2.4/"+post_id+"/comments"
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        print response

#print(read_posts(time,token))
post_comment(msg,token)
