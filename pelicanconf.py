#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Quack1'
SITENAME = u'Quack1@Blog'
SITEURL = 'http://quack1.no-ip.org'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

THEME = "notmyidea"

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/_Quack1'),)
GOOGLE_ANALYTICS = 'UA-35393252-1'

DEFAULT_PAGINATION = 10
STATIC_PATHS = ["upload"]

# Timezone
PLUGINS=['pelican.plugins.sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.75,
        'pages': 0.75
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}
