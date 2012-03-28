# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://acrylamid.readthedocs.org/en/latest/conf.py.html

SITENAME = 'sebix'
WWW_ROOT = 'http://sebix.github.com/'

AUTHOR = 'sebix'
EMAIL = 'info@example.org' # not used anywhere

# hyphenate is needed for nice justification
FILTERS = ['markdown+codehilite(css_class=highlight)', 'hyphenate', 'typo']
VIEWS = {
    '/': {'filters': ['summarize', 'h1'],
          'pagination': '/page/:num',
          'view': 'index'},
    '/:year/:slug/': {'filters': ['h1'], 'view': 'entry'},
    '/atom/': {'filters': ['h2'], 'view': 'atom'},
    '/rss/': {'filters': ['h2'], 'view': 'rss'},
    '/articles/': {'view': 'articles'},
    #'/atom/full': {'filters': ['h2'], 'view': 'atom', 'num_entries': 1000},
    '/tag/:name/': {'filters': ['h1', 'summarize'], 'view':'tag',
                   'pagination': '/tag/:name/:num'},
    }

PERMALINK_FORMAT = '/:year/:slug/index.html'
DATE_FORMAT = '%d.%m.%Y, %H:%M'
