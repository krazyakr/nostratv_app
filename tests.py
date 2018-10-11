import api as API

events = API.GetEventsFromSource('nflfullhd')['events']
event = API.GetEventData( events[1] )['event']

print 'Name: ' + event['title']
print 'id: ' + event['id']
for stream in event['streams']:
    print "Name: {0} Links: {1}".format(stream['name'], str(stream['links']))