from instagram.client import InstagramAPI
import sys
import urllib2
import json

instagramkey = '42d923adac4743019cbfb278dd433114'
recent_media, next_ = api.user_recent_media()
photos = []
for media in recent_media:
    photos.append('<img src="%s"/>' % media.images['thumbnail'].url)

with open("output_IG_Data.csv", "w") as out_file:
	for i in range(length(photos)):
		print i
client_id = '42d923adac4743019cbfb278dd433114'
client_secret = '63c0b209a0e846d3b8ac96400c030fd3'
access_token = 'https://api.instagram.com/oauth/authorize/?client_id=42d923adac4743019cbfb278dd433114&redirect_uri=http://kakorrhaphio.github.io&response_type=code'
client_ip = '128.172.48.160'
api = InstagramAPI(client_id=client_id, client_secret=client_secret,client_ips= client_ip,access_token= access_token)

authUrl = 'https://instagram.com/oauth/authorize/?client_id=42d923adac4743019cbfb278dd433114&redirect_uri=http://kakorrhaphio.github.io&response_type=token'

access_token = "42d923adac4743019cbfb278dd433114"
client_secret = "63c0b209a0e846d3b8ac96400c030fd3"
api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="userid", count=20)

for media in recent_media:

   print media.caption.text


if len(sys.argv) > 1 and sys.argv[1] == 'local':
    try:
        from test_settings import *

        InstagramAPI.host = test_host
        InstagramAPI.base_path = test_base_path
        InstagramAPI.access_token_field = "access_token"
        InstagramAPI.authorize_url = test_authorize_url
        InstagramAPI.access_token_url = test_access_token_url
        InstagramAPI.protocol = test_protocol
    except Exception:
        pass


        try:
            import __builtin__
            input = getattr(__builtin__, 'raw_input')
        except (ImportError, AttributeError):
            pass

            client_id = input("Client ID: ").strip()
            client_secret = input("Client Secret: ").strip()
            redirect_uri = input("Redirect URI: ").strip()
            raw_scope = input("Requested scope (separated by spaces, blank for just basic read): ").strip()
            scope = raw_scope.split(' ')


            if not scope or scope == [""]:
                scope = ["basic"]

                api = InstagramAPI(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
                redirect_uri = api.get_authorize_login_url(scope = scope)

                print ("Visit this page and authorize access in your browser: "+ redirect_uri)

                code = (str(input("Paste in code in query string after redirect: ").strip()))

                access_token = api.exchange_code_for_access_token(code)
                print ("access token: " )
                print (access_token)



all_media_ids = []
media_ids, next = api.tag_recent_media (tag_name = 'capitalone', count = 30)
temp, max_tag = next.split('max_tag_id=')
max_tag = str(max_tag)

for media_id in media_ids:
	all_media_ids.append(media_id.id)
print all_media_ids
print len(all_media_ids)
counter = 1

while next and counter < 3:
more_media, next = api.tag_recent_media(tag_name = 'capitalone', max_tag_id = max_tag)
temp,max_tag = next.split('max_tag_id=')
max_tag = str(max_tag)
for media_id2 in more_media:
	all_media_ids.append(media_id2.id)
counter+= 1

media_all_ids = list(OrderedDict.fromkeys(media_all_ids))

print len(media_all_ids)

