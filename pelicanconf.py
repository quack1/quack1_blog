#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Quack1'
SITENAME = u'Quack1☠Blog'
SIDEBAR_DIGEST = u'Blog-Notes of a Linux/Security/Hacking guy'
SITEURL = 'http://quack1.me'
RELATIVE_URLS = True
FEED_DOMAIN = SITEURL
AVATAR = u'upload/avatar.png'

TIMEZONE = 'Europe/Paris'
DATE_FORMATS = {
    'fr' : '%d/%m/%Y',
    'en' : '%d/%m/%Y',
}
DEFAULT_LANG = u'fr'

#THEME = "notebook"
THEME = "./themes/notebook"
PDF_GENERATOR = False

# Blogroll

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/_Quack1'),('Mail', 'mailto:blog@quack1.me'))
TWITTER_USERNAME = "_Quack1"

BLOGROLL = (
    ('Zythom', 'http://zythom.blogpost.com'),
    ('Sid', 'http://sid.rstack.org/blog'),
    ('Korben', 'http://korben.info'),
    ('Le Blog des Nouvelles Technologies', 'http://blognt.fr'),
    ('Commit Strip', 'http://www.commitstrip.com/fr/'),
    ('Planet-Libre', 'http://www.planet-libre.org/'),
    ('Planet-Ubuntu', 'http://planet.ubuntu-fr.org/'),
    ('Conix Security', 'http://conixsecurity.fr/'),
    ('GCU-Squad', 'http://www.gcu-squad.org/'),
    ('La Grotte Du Barbu', 'http://lagrottedubarbu.com/'),
    ('JcFrog', 'http://jcfrog.com/blog/')
    )

DEFAULT_PAGINATION = 10
STATIC_PATHS = ["upload"]
DISPLAY_PAGES_ON_MENU = "True"

FEED_ATOM = 'feeds/all.atom.xml'
FEED_ALL_ATOM = 'feeds/all.all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category_%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag_%s.atom.xml'

# Tag Cloud
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 1000

# Extensions
PLUGINS = ['pelican.plugins.sitemap','pelican.plugins.global_license']
MD_EXTENSIONS = ['headerid', 'codehilite(css_class=highlight)', 'footnotes']

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

EXTRA_PATH_METADATA = { 'extras/robots.txt': {'path': 'robots.txt'},
                   	'extras/humans.txt': {'path': 'humans.txt'}}
