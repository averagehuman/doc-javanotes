
import os
from os.path import join as pathjoin, exists as pathexists, dirname, basename
import re

JAVA_CODE_BLOCK = '.. code-block:: java\n'
division_patt = re.compile(r'`(?P<type>Section|Chapter)(?P<chapter>\d+)(?P<section>[.]\d+)?`_')
def on_division_link(m):
    chapter = m.group('chapter')
    section = m.group('section')
    d = dict(
        divtype=m.group('type'),
    )
    if section:
        section = section.lstrip('.')
        return ':doc:`Section %s.%s</%s/s%s>`' % (chapter, section, chapter, section)
    else:
        return ':doc:`Chapter %s</%s/index>`' % (chapter, chapter)

for root, dirs, files in os.walk('en'):
    for f in files:
        if f.endswith('.rst'):
            orig_path = root + '/' + f
            tmp_path = orig_path + '.tmp'
            with open(orig_path) as orig:
                with open(tmp_path, 'wb') as tmp:
                    for line in orig:
                        if line.strip() == '::':
                            tmp.write(JAVA_CODE_BLOCK)
                            continue
                        tmp.write(division_patt.sub(on_division_link, line))
                    os.rename(tmp_path, orig_path)
                    print orig_path

