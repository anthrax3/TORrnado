__author__ = 'TzAnAnY'

from monkey import patch_socks
patch_socks()

from tornado.curl_httpclient import CurlAsyncHTTPClient
from tornado.ioloop import IOLoop
from pycurl import PROXYTYPE_SOCKS5


def handle_request(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body
    IOLoop.instance().stop()


if __name__ == '__main__':
    config = {
        'proxy_type': PROXYTYPE_SOCKS5,
        'proxy_host': '127.0.0.1',
        'proxy_port': 9050,
        'validate_cert': False
    }
    client = CurlAsyncHTTPClient()
    # for i in range(5):
    client.fetch("https://www.dyndns.org/", handle_request, **config)
    IOLoop.instance().start()
    client.close()
