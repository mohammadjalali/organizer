import os
import sys
import re
from numpy import unique

username = sys.argv[1]

path = 'ls /home/{}/Desktop'.format(username)

f = os.popen(path).read()

formats = re.findall(r"\..*", f)

formats = unique(formats)

for fmt in formats:
    _ = fmt[1:]
    os.system('mkdir /home/mohammad/Desktop/{}'.format(_))
    a = re.findall(r"..*\.{}".format(_), f)
    a = unique(a)
    print(a)
    for fi in a:
        os.system('mv /home/mohammad/Desktop/{} /home/mohammad/Desktop/{}'.format(fi, _))