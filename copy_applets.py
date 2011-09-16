
import os
from os.path import exists as pathexists, join as pathjoin, basename, dirname, abspath
import shutil

for root, dirs, files in os.walk('tmp/javanotes6-web-site'):
    for f in files:
        if f.endswith('.jar') or f.endswith('.class'):
            chapter = basename(root)[1:]
            src = pathjoin(root, f)
            dst = pathjoin('javanotes', chapter, 'applets', f)
            dir = dirname(dst)
            if not pathexists(dir):
                os.makedirs(dir)
            print dst
            shutil.copyfile(src, dst)

