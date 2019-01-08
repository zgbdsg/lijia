#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(host='127.0.0.1', dbn='mysql', db='todo', user='root', pw='Admin@123')
#db = web.database(host='127.0.0.1', dbn='mysql', db='todo', user='root', pw='')

render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    email='zgbdsg@gmail.com',
    site_name='zhidian',
    site_desc='',
    static='/static',
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
