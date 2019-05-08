#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yu Zhai'
SITENAME = u'zhaiyuSCI'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['img']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ( ('Prof. Hui Li Group', 'https://huiligroup.org/'),
         )

# Social widget
SOCIAL = (
        ('linkedin', 'https://www.linkedin.com/in/yu-zhai-1ba26291'),
          ('github', 'https://github.com/zhaiyusci'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "./pelican-blue"
