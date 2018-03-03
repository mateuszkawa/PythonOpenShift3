#!/usr/bin/env python
import tornado
import tornado.httpclient

from tornado import gen
from tornado.web import asynchronous


class SearchHandler(tornado.web.RequestHandler):
    client = tornado.httpclient.AsyncHTTPClient()

    @gen.engine
    def get(self: tornado.web.RequestHandler):
        self.finish({'text': "Hello World"})


handlers = [(r'/searchs', SearchHandler), ]
