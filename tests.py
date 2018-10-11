import api as API

events = API.GetEventsFromSource('nflfullhd')['events']
event = API.GetEventData( events[0] )['event']

print ''
print 'Name: ' + event['title']
print 'id: ' + event['id']
print ''
for stream in event['streams']:
    print "\tName: {0}".format(stream['name'])
    for link in stream['links']:
        print "\t\tId: {0}\tlink: {1}".format( link['id'], link['self'] )

        _stream = API.GetStream(link)
        if(_stream != None and 'stream' in _stream ):
            _stream = _stream['stream']
            if( 'links' in _stream ):
                for _link in _stream['links']:
                    print '\t\t\t{0} - {1}'.format( _link['name'], _link['url'] )