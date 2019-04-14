#!/usr/bin/env python3

import os

path = os.path.abspath('.')

date_from_name = {}
for name in os.listdir(path):
    fullname = os.path.join(path, name)
    if os.path.isfile(fullname):
        date_from_name[fullname] = os.path.getatime(fullname)


for path, time in date_from_name.items():
    print('{0:.<25}{1}'.format(time, path))
