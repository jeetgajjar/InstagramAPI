from instagram.client import InstagramAPI

client_id = '42d923adac4743019cbfb278dd433114'
client_secret = '63c0b209a0e846d3b8ac96400c030fd3'
access_token = 'https://api.instagram.com/oauth/authorize/?client_id=42d923adac4743019cbfb278dd433114&redirect_uri=http://kakorrhaphio.github.io&response_type=code'
client_ip = '128.172.48.160'
api = InstagramAPI(client_id=client_id, client_secret=client_secret,client_ips= client_ip,access_token= access_token)
