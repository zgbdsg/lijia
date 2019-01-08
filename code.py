#!/usr/bin/env python
# coding: utf-8
from config.url import urls
import web

web.config.debug = False
app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))
web.config._session = session

if __name__ == "__main__":
    app.run()
