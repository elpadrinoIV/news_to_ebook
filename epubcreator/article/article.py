import urllib2
import urllib
from cookielib import CookieJar
from lxml import html,etree
from epubcreator.xmlutils import *

class Article:
    def __init__(self, link):
        self.original_link_ = link

    def preprocess(self, page):
        # as default, if there is one and only one article element, keep just that
        body = page.xpath("//body")[0]

        articles = body.xpath(".//article")

        print "Body has " + str(len(articles)) + " articles"
        if len(articles) == 1:
            article = articles[0]
            body.clear()
            body.append(article)


    def remove_unwanted_elements(self, page):
        wanted = ['article', 'section', 'main', 'header',
                'body', 'head', 'html', 'title',
                'abbr', 'acronym', 'address', 'blockquote', 'br', 
                'cite', 'code', 'dfn', 'div', 'em',
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'kbd', 'p',
                'pre', 'q', 'samp', 'span', 'strong', 'var',
                'a', 'dl', 'dt', 'dd', 'ol', 'ul', 'li',
                'b', 'big', 'hr', 'i', 'small', 'sub', 'sup', 'tt',
                'caption', 'col', 'colgroup', 'table', 'tbody', 'td',
                'tfoot', 'th', 'thead', 'tr']

        keep_only_wanted(page, wanted)

        for elem in page.xpath("//*[@style='display:none']"):
            remove_element(elem)

        for elem in page.xpath("//*[contains(@class, 'robots-nocontent')]"):
            remove_element(elem)


    def sanitize(self, page):
        for elem in page.xpath(".//article|.//section|.//header|.//main"):
            elem.tag = 'div'



    def generate_epub_article(self, path):
        cj = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        parser = etree.HTMLParser(remove_comments=True)
        page = html.fromstring(opener.open(self.original_link_).read(), parser=parser)
        self.preprocess(page)

        self.remove_unwanted_elements(page)
        #self.sanitize(page)
        #remove_all_attributes(page)

        link = html.Element('a')
        link.text = "Original source: " + self.original_link_
        link.attrib['href'] = self.original_link_

        page.xpath('//body')[0].append(link)

        output_file = open(path, 'w')
        output_file.write(html.tostring(page, pretty_print=True))
        output_file.close()

class LaNacionArticle(Article):
    def __init__(self, link):
        Article.__init__(self, link)

    def preprocess(self, page):
        # as default, if there is one and only one article element, keep just that
        body = page.xpath("//body")[0]

        encabezado = body.xpath("//*[@id='encabezado']")[0]
        cuerpo = body.xpath("//*[@id='cuerpo']")[0]

        body.clear()
        body.append(encabezado)
        body.append(cuerpo)
