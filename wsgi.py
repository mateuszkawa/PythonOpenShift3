#!/usr/bin/env python
import os

#
# Below for testing only
#
if __name__ == '__main__':
    ip = 'localhost'
    port = 8059

    from wsgi.openshift import handlers
    import tornado.web

    settings = {
        'static_path': os.path.join(os.getcwd(), 'wsgi/static'),
        'template_path': os.path.join(os.getcwd(), 'wsgi/templates'),
    }

    application = tornado.web.Application(handlers, **settings)
    application.listen(port)
    print('Service listen on %s' % port)
    tornado.ioloop.IOLoop.instance().start()
