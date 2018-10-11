import urllib2,json
import log

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0', 'Accept-Charset': 'utf-8;q=0.7,*;q=0.7', 'Content-Type': 'application/json'}
__baseUrl = 'http://rmtorres.no-ip.info'
__eventsUrl = __baseUrl + '/events/'

# Gets the contents of the given url
# Returns the result as a string
def __getContent(url, requestHeaders=None):
    if requestHeaders == None:
        requestHeaders = headers

    try:
        log.d("GET - {0} [{1}]".format(url, requestHeaders))
        response = urllib2.urlopen(urllib2.Request(url, headers=requestHeaders))

        result = response.read()
        # log.d("RESPONSE - {0}".format(result))
        
        return result
    except urllib2.URLError as error:
        log.e( str(error) )
        return None


def GetEventsFromSource(source):
    url = __eventsUrl + source

    response = __getContent(url)
    
    if response != None:
        return json.loads(response)
    else:
        return None

def GetEventData(eventJson):
    url = __baseUrl + eventJson['self']

    response = __getContent(url)
    
    if response != None:
        return json.loads(response)
    else:
        return None

def GetStream(linkJson):
    url = __baseUrl + linkJson['self']

    response = __getContent(url)
    
    if response != None:
        return json.loads(response)
    else:
        return None