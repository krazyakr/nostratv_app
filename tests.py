import api as API
import os

events = API.GetEventsFromSource('nflfullhd')

os.system('clear')
print '****************************************'
print '*           NFL Full Games             *'
print '****************************************'
index = 0
for event in events:
    print '*  {0}\t-  {1}'.format(str(index), event['title'])
    index = index + 1

print '****************************************'
selected = raw_input("* > ")

event = events[int(selected)]

os.system('clear')
print '****************************************'
print 'You selected \'{0}\''.format(event['title'])
print '****************************************'

eventData = API.GetEventData(event)
print str(eventData)

print '****************************************'
print '*             Streams                  *'
print '****************************************'
streams = eventData['streams']
index = 0
for stream in streams:
    print '* {0}\t- {1}'.format(str(index), stream['name'])
    index = index + 1

print '****************************************'
selected = raw_input("* > ")

stream = streams[int(selected)]
os.system('clear')
print '****************************************'
print 'You selected \'{0}\' from \'{1}\''.format(stream['name'], event['title'])
print '****************************************'

links = stream['links']
index = 0
for link in links:
    print '* {0}\t- {1}'.format(str(index), link['id'])
    index = index + 1
print '****************************************'
selected = raw_input("* > ")

link = links[int(selected)]
os.system('clear')
print '****************************************'
print 'You selected \'{0} | {1}\' from \'{2}\''.format(stream['name'], link['id'], event['title'])
print '****************************************'

streamDetail = API.GetStream(link)
print str(streamDetail)

streamLinks = streamDetail['links']
index = 0
for link in streamLinks:
    print '* {0}\t- {1}'.format(str(index), link['name'])
    index = index + 1
print '****************************************'
selected = raw_input("* > ")

streamLink = streamLinks[int(selected)]

print streamLink['url']
