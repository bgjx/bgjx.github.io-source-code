
#============== GENERAL===================
AUTHOR = 'Me'
SITENAME = 'BGJX blogspot'
SITEURL = 'https://bgjx.github.io/blogs/'
STATIC_PATHS=['notebooks','images']
TIMEZONE = 'Asia/Jakarta'
DEFAULT_LANG = 'en'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
MARKUP = ('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"] 
THEME='theme/pelican-bootstrap3'



#============== LIST OF PLUGINS ===================
PLUGIN_PATHS=['pelican-plugins', 'pelican-plugins/tipue_search/pelican/plugins/tipue_search']
PLUGINS = ['sitemap','pelican-ipynb.markup',
           'i18n_subsites', 'related_posts',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'tipue_search',
           'summary', 'feed_summary',
           'liquid_tags.notebook'
           ]





#============== ICON SITES===================
SITELOGO = 'images/favicon.png'
SITELOGO_SIZE='2rem'
FAVICON = 'images/favicon.png'




#============== Jupyter NoteBook Special Settings===================
NOTEBOOK_DIR = 'notebooks'


#============== DIRECT TEMPLATE ===================
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

SEARCH_URL='https://bgjx.github.io/blogs/search.html'



#============== PAGE SETINGS ===================
#ARCHIVE PAGES
DISPLAY_ARCHIVE_ON_SIDEBAR=True
MONTH_ARCHIVE_SAVE_AS='archives/{date:%Y}/{date:%m}/index.html'
DISPLAY_CATEGORY_IN_BREADCRUMBS=True



# INDEX PAGE
DISPLAY_ARTICLE_INFO_ON_INDEX= True

#ABOUT
ABOUT_ME = 'I am a Geophysical Engineer who loves programming and arts'
AVATAR='images/avatar.jpg'

#SIDE BAR
DISPLAY_TAGS_ON_SIDEBAR=True
DISPLAY_TAGS_INLINE=True
DISPLAY_CATEGORIES_ON_SIDEBAR=True
DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
RECENT_POST_COUNT=True
DISPLAY_ARCHIVE_ON_SIDEBAR=True
DISPLAY_AUTHORS_ON_SIDEBAR=True
PADDED_SINGLE_COLUMN_STYLE=False

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}
    
    


#================= ARTICLE & PAGE SAVE AS===========%
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}.html'




#Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home','https://bgjx.github.io/index.html'),
         ('About Me','https://bgjx.github.io/contents/about.html'),
         ('Blogs', 'https://bgjx.github.io/blogs/'),
         ('Arts', 'https://bgjx.github.io/contents/arts.html')
         )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/zakki_edelo'),
          ('linkedin', 'https://www.linkedin.com/in/arhamzakki'),
          ('github', 'https://github.com/arham99'),
          ('instagram', 'https://www.instagram.com/edelo_arham'))

#DISQUS
DISQUS_NO_ID=True

ENABLE_MATHJAX = True
DEFAULT_PAGINATION = 5

#LICENSE
CC_LICENSE_DERIVATIVES="yes"

#Addthis
ADDTHIS_PROFILE=True

#DISQUS
DISQUS_SITENAME='bgjx-blogs'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
