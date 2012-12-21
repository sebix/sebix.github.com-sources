# -*- encoding: utf-8 -*-
# This is your config file.  Please write in a valid python syntax!
# See http://acrylamid.readthedocs.org/en/latest/conf.py.html

SITENAME = 'sebix'
WWW_ROOT = 'http://sebix.github.com/'

AUTHOR = 'sebix'
EMAIL = 'info@example.org' # not used anywhere

# hyphenate is needed for nice justification
#FILTERS = ['markdown+codehilite(css_class=highlight)+mathml', 'hyphenate', 'typo', 'h1']
FILTERS = ['textile', 'hyphenate+5', 'typo', 'h1', 'metalogo']
VIEWS = {
    '/': {'filters': ['summarize', 'h1'],
          'pagination': '/page/:num',
          'view': 'index',
          'condition': lambda e: '!gallery!' not in e.tags},
    '/:year/:slug/': {'filters': ['h1'],
        'view': 'entry',
        'condition': lambda e: '!gallery!' not in e.tags},
    '/atom/': {'filters': ['h2'],
        'view': 'atom',
        'condition': lambda e: '!gallery!' not in e.tags},
    '/rss/': {'filters': ['h2'],
        'view': 'rss',
        'condition': lambda e: '!gallery!' not in e.tags},
    '/articles-chrono/': {'view': 'articles',
        'condition': lambda e: '!gallery!' not in e.tags},
    '/atom/full': {'filters': ['h2'],
        'view': 'atom',
        'num_entries': 1000,
        'condition': lambda e: '!gallery!' not in e.tags},
    '/tag/:name/': {'filters': ['h1', 'summarize'],
        'view':'tag',
        'pagination': '/tag/:name/:num',
        'condition': lambda e: '!gallery!' not in e.tags},
    "sitemap.xml": {"view": "Sitemap"},
    "/gallery/" : {'view': 'index',
        'pagination': '/gallery/:num/',
#        'filters': ['intro'],
        'condition': lambda e: '!gallery!' in e.tags},
    '/gallery/:year/:slug/': {'filters': ['h1'],
        'view': 'entry',
        'condition': lambda e: '!gallery!' in e.tags},
    '/gallery/atom/': {'filters': ['h2'],
        'view': 'atom',
        'condition': lambda e: '!gallery!' in e.tags},
    '/gallery/rss/': {'filters': ['h2'],
        'view': 'rss',
        'condition': lambda e: '!gallery!' in e.tags},
    '/gallery/atom/full': {'filters': ['h2'],
        'view': 'atom',
        'num_entries': 1000,
        'condition': lambda e: '!gallery!' in e.tags},
    '/gallery/tag/:name/': {'filters': ['h1', 'summarize'],
        'view':'tag',
        'pagination': '/tag/:name/:num',
        'condition': lambda e: '!gallery!' in e.tags},
    }

SUMMARIZE_LINK = '<span>&#8230; <a href="%s" class="continue">continue</a></span>'

PERMALINK_FORMAT = '/:year/:slug/index.html'
DATE_FORMAT = '%d.%m.%Y, %H:%M'
LANG = "en_US.UTF-8"

DEPLOYMENT = {
	"ls": "ls",
	"status": "cd %s && git status",
	'diff': 'cd %s && git diff',
	'push': 'cd %s && git push',
#	'rm': 'rm -r %s/2012/ %s/articles/ %s/atom/ %s/guest-articles/ %s/projects/ %s/rss %s/tag/ %s/index.html',
}

OUTPUT_IGNORE = ['files/', 'img/', 'favicon.ico', 'css/', 'js/', '.*', '.*/']
CONTENT_IGNORE = ['drafts/*', '.*']
ACRONYMS_FILE = 'layouts/acronyms.txt'
