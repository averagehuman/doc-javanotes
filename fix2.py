
import os
from os.path import join as pathjoin, exists as pathexists, dirname, basename
import re

JAVA_CODE_BLOCK = '.. code-block:: java\n'
nav_marker = "`Chapter Index`_ | `Main Index`_"

for root, dirs, files in os.walk('javanotes'):
    for f in files:
        if f.startswith('quiz') and f.endswith('.rst'):
            origpath = pathjoin(root, f)
            tmppath = origpath + '.tmp'
            with open(origpath) as orig:
                with open(tmppath, 'wb') as tmp:
                    orig.next()
                    orig.next()
                    for line in orig:
                        if nav_marker in line:
                            break
                        stripped = line.strip()
                        if stripped.startswith('Question') and stripped.endswith(':'):
                            line = stripped[:-1]
                            line = '\n\n' + line + '\n' + '~'*len(line) + '\n\n'
                        elif stripped.startswith('Answer') and stripped.endswith(':'):
                            line = stripped[:-1]
                            line = '\n\n' + line + '\n' + "^"*len(line) + '\n\n'
                        elif stripped == '::':
                            line = JAVA_CODE_BLOCK
                        tmp.write(line)
            os.rename(tmppath, origpath)
            print origpath
                            
