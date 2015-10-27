from instagram.client import InstagramAPI

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
