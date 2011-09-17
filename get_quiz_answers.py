
import os

root_url = 'http://math.hws.edu/javanotes/'

for i in range(1, 14):
    src = '%s/c%s/quiz_answers.html' % (root_url, i)
    dst = 'javanotes/%s/quiz_answers.rst' % i
    print dst
    os.system('orb html2rest %s > %s' % (src, dst))


