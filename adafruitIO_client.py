from Adafruit_IO import Client, RequestError, Feed
ADAFRUIT_IO_KEY = 'aio_eYsz18mwDt7Vn2SbB3NGSCEfaN1Y'
ADAFRUIT_IO_USERNAME = 'allanromanreyes'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY) #instantiate client

try:
    test_feed = aio.feeds('test-feed')
except RequestError:
    test = Feed(name='test-feed')
    test_feed = aio.create_feed(test)
    
aio.send_data(test_feed.key, "TEXTSTRING") #sends data

data = aio.receive(test_feed.key) #prints results of SEND data
print('Latest value from Test: {0}'.format(data.value))
print('Recieved value from test feed has the following metadata: {0}'.format(data))