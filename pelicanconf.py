#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Quack1'
SITENAME = u'Quack1@Blog'
SIDEBAR_DIGEST = u'Blog-Notes of a random Linux/Security/Hack guy'
SITEURL = 'http://quack1.no-ip.org'
RELATIVE_URLS = False
FEED_DOMAIN = SITEURL
AVATAR = u'static/upload/avatar.png'

TIMEZONE = 'Europe/Paris'
DATE_FORMATS = {
    'fr' : '%d/%m/%Y',
    'en' : '%d/%m/%Y',
}
DEFAULT_LANG = u'fr'

THEME = "themes/notebook"
PDF_GENERATOR = False

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/_Quack1'),('Mail', 'mailto:quack1blog@gmail.com'))
GOOGLE_ANALYTICS = 'UA-35393252-1'
DISQUS_SITENAME = 'quack1blog'
TWITTER_USERNAME = "_Quack1"

DEFAULT_PAGINATION = 10
STATIC_PATHS = ["upload"]
DISPLAY_PAGES_ON_MENU = "True"

FEED_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'

# Tag Cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 10

# Timezone
PLUGINS=['pelican.plugins.sitemap','pelican.plugins.global_license']

# Firefox Affiliates
FIREFOX_BANNERS = (('35549', '/theme/images/download_firefox.png', u'Télécharger Firefox : facile, amusant, génial'),
                    ('36259', '/theme/images/download_firefox_android.png', u'Firefox for Android'))

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

COPYRIGHT="""
/*
 * ----------------------------------------------------------------------------
 * "THE BEER-WARE LICENSE" (Revision 42):
 * <phk@FreeBSD.ORG> wrote this file. As long as you retain this notice you
 * can do whatever you want with this stuff. If we meet some day, and you think
 * this stuff is worth it, you can buy me a beer in return Poul-Henning Kamp
 * ----------------------------------------------------------------------------
 */
"""
