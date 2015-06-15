#!/usr/bin/python

from epubcreator.article import article

link = 'http://www.lanacion.com.ar/1801751-demolicion-puente-general-paz-video-25-de-mayo'
link2 = 'http://www.nytimes.com/2015/06/15/world/middleeast/us-airstrike-targets-qaeda-operative-in-libya.html'

article = article.Article(link2)
article.generate_epub_article('prueba2.html')


