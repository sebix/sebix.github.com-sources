# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

SITENAME = 'sebix'
WWW_ROOT = 'https://www.sebix.at/'

AUTHOR = 'sebix'
EMAIL = 'sebix@sebix.at'

FILTERS = ['textile+codehilite(css_class=highlight)', 'hyphenate+5', 'typo',
           'h1', 'metalogo']
"""
VIEWS = {
    "/:slug/": {"view": "page"},
    '/': {'filters': ['summarize', 'h1'], # TODO: h1?
          'pagination': '/page/:num',
          'view': 'index'},
    '/:year/:slug/': {'filters': ['h1'], # TODO: h1? {'views': ['entry', 'draft']},
        'view': 'entry'},
    '/atom/': {'filters': ['h2'],
        'view': 'atom'},
    '/rss/': {'filters': ['h2', 'nohyphenate'],
        'view': 'rss'},
    '/articles-chrono/': {'view': 'articles'},
    '/atom/': {'filters': ['h2', 'nohyphenate'],
        'view': 'atom',
        'num_entries': 1000},
    '/tag/:name/': {'filters': ['h1', 'summarize'], # TODO: h1?
        'view':'tag',
        'pagination': '/tag/:name/:num'},
    "sitemap.xml": {"view": "Sitemap"},
    }
"""
VIEWS = {
    '/': {
        'filters': ['summarize', 'h2'],
        'pagination': '/page/:num',
        'view': 'index',
        'if': lambda e: '!gallery!' not in e.tags},
    '/:year/:slug/': {
        'filters': ['h2'],
        'view': 'entry',
        'if': lambda e: '!gallery!' not in e.tags},
    '/atom/': {
        'filters': ['h2'],
        'view': 'atom',
        'if': lambda e: '!gallery!' not in e.tags},
    '/rss/': {
        'filters': ['h2'],
        'view': 'rss',
        'if': lambda e: '!gallery!' not in e.tags},
    '/articles-chrono/': {
        'view': 'articles',
        'if': lambda e: '!gallery!' not in e.tags},
    '/atom/full': {
        'filters': ['h2'],
        'view': 'atom',
        'num_entries': 1000,
        'if': lambda e: '!gallery!' not in e.tags},
    '/tag/:name/': {
        'filters': ['h2', 'summarize'],
        'view':'tag',
        'pagination': '/tag/:name/:num',
        'if': lambda e: '!gallery!' not in e.tags},
    'sitemap.xml': {
        'view': 'Sitemap'},
    "/:slug/": {"view": "page"}
#   '/gallery/' : {
#        'view': 'index',
#        'pagination': '/gallery/:num/',
#        'if': lambda e: '!gallery!' in e.tags},
#    '/gallery/:year/:slug/': {
#        'filters': ['h1'],
#        'view': 'entry',
#        'if': lambda e: '!gallery!' in e.tags},
#    '/gallery/atom/': {
#        'filters': ['h2'],
#        'view': 'atom',
#        'if': lambda e: '!gallery!' in e.tags},
#    '/gallery/rss/': {
#        'filters': ['h2'],
#        'view': 'rss',
#        'if': lambda e: '!gallery!' in e.tags},
#    '/gallery/atom/full': {
#        'filters': ['h2'],
#        'view': 'atom',
#        'num_entries': 1000,
#        'if': lambda e: '!gallery!' in e.tags},
#    '/gallery/tag/:name/': {
#        'filters': ['h1', 'summarize'],
#        'view':'tag',
#        'pagination': '/tag/:name/:num',
#        'if': lambda e: '!gallery!' in e.tags},
    }

THEME = 'layouts'
DATE_FORMAT = '%Y-%m-%d, %H:%M'

SUMMARIZE_LINK = '<span>&#8230; <a href="%s" class="continue">continue</a></span>'

PERMALINK_FORMAT = '/:year/:slug/index.html'
LANG = "en_US.UTF-8"

OUTPUT_IGNORE = ['files/', 'img/', 'favicon.ico', 'css/', 'js/', '.*', '.*/', '*~']
CONTENT_IGNORE = ['drafts/*', '.*', '*~']
ACRONYMS_FILE = 'layouts/acronyms.txt'
