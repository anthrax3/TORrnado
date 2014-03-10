__author__ = 'TzAnAnY'

SAVED = {}


def patch_item(module, attr, new_item):
    obj = object()
    old_item = getattr(module, attr, obj)
    if old_item is not obj:
        SAVED.setdefault(module.__name__, {}).setdefault(attr, old_item)
    setattr(module, attr, new_item)


def patch_socks():
    from .httpclient import HTTPRequest
    import tornado.httpclient
    patch_item(tornado.httpclient, 'HTTPRequest', HTTPRequest)

    from .curl_httpclient import CurlAsyncHTTPClient
    import tornado.curl_httpclient
    patch_item(tornado.curl_httpclient, 'CurlAsyncHTTPClient', CurlAsyncHTTPClient)

