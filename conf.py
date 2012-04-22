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
          'view': 'index'},
    '/:year/:slug/': {'filters': ['h1'], 'view': 'entry'},
    '/atom/': {'filters': ['h2'], 'view': 'atom'},
    '/rss/': {'filters': ['h2'], 'view': 'rss'},
    '/articles-chrono/': {'view': 'articles'},
    '/atom/full': {'filters': ['h2'], 'view': 'atom', 'num_entries': 1000},
    '/tag/:name/': {'filters': ['h1', 'summarize'], 'view':'tag',
                   'pagination': '/tag/:name/:num'},
    }

PERMALINK_FORMAT = '/:year/:slug/index.html'
DATE_FORMAT = '%d.%m.%Y, %H:%M'
LANG = "en_US"

DEPLOYMENT = {
	"ls": "ls",
	"status": "cd %s && git status",
	'diff': 'cd %s && git diff',
	'push': 'cd %s && git push',
	'rm': 'rm -r %s/2012/ %s/articles/ %s/atom/ %s/guest-articles/ %s/projects/ %s/rss %s/tag/ %s/index.html',
}

OUTPUT_IGNORE = ['files/', 'img/', 'favicon.ico', 'style.css', '.*', '.*/']
ENTRIES_IGNORE = ['drafts/*']
ACRONYMS_FILE = 'layouts/acronyms.txt'
