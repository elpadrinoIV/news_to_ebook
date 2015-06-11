import urllib
from lxml import html,etree



class Article:
    def __init__(self, link):
        self.original_link_ = link

    def generate_epub_article(self, path):
        page = html.fromstring(urllib.urlopen(self.original_link_).read())

        wanted = ['article', 'section', 'header', 
                'body', 'head', 'html', 'title',
                'abbr', 'acronym', 'address', 'blockquote', 'br', 
                'cite', 'code', 'dfn', 'div', 'em',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'kbd', 'p',
                'pre', 'q', 'samp', 'span', 'strong', 'var',
                'a', 'dl', 'dt', 'dd', 'ol', 'ul', 'li',
                'b', 'big', 'hr', 'i', 'small', 'sub', 'sup', 'tt',
                'caption', 'col', 'colgroup', 'table', 'tbody', 'td',
                'tfoot', 'th', 'thead', 'tr']

