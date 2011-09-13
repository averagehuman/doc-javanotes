
import os
from os.path import join as pathjoin, exists as pathexists, dirname, basename
import re

root_url = 'http://math.hws.edu/javanotes/'

patt = re.compile(r'href="(?P<href>c(?P<chapter>\d+)/(?P<section>.+?).html)"')

with open('toc.html') as toc:
    text = toc.read()
    for match in patt.finditer(text):
        dir = 'en/' + match.group('chapter')
        if not pathexists(dir):
            os.makedirs(dir)
        dest = dir + '/' + match.group('section') + '.rst'
        url = root_url + match.group('href')
        print url
        os.system('orb html2rest %s > %s' % (url, dest))

for name in ['preface', 'glossary']:
    os.system('orb html2rest %s%s.html > en/%s.rst' % (root_url, name, name))
