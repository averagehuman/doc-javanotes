
import os
from os.path import join as pathjoin, exists as pathexists, dirname, basename
import re

alphabetic = re.compile(r'\w')
nav_marker = "`Chapter Index`_ | `Main Index`_"

for root, dirs, files in os.walk('javanotes'):
    for f in files:
        if f.startswith('s') and f.endswith('.rst'):
            orig_path = root + '/' + f
            tmp_path = orig_path + '.tmp'
            section_id = section_name = underline = None
            with open(orig_path) as orig:
                with open(tmp_path, 'wb') as tmp:
                    while True:
                        try:
                            line = orig.next()
                        except StopIteration:
                            break
                        if not section_id:
                            if line.startswith('Section '):
                                section_id = line.strip().split()[-1]
                            continue
                        if not section_name and alphabetic.match(line):
                            section_name = line.strip()
                            try:
                                underline = orig.next().strip()
                            except StopIteration:
                                break
                            underline += underline[0] * (len(section_id)+2)
                            break
                    if section_id and section_name and underline:
                        tmp.write('\n%s. %s\n%s\n' % (section_id, section_name, underline))
                        for line in orig:
                            if line and line[0] == '[' and '|' in line:
                                break
                            tmp.write(line)
                        os.rename(tmp_path, orig_path)
                        print orig_path

