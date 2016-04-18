#!/usr/bin/env python

"""
Update all the packages (in alphabetical order)
that you have installed globally with pip
"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import os

import pip


dists = []
for dist in pip.get_installed_distributions():
    dists.append(dist.project_name)

dists = sorted(dists, key=lambda s: s.lower())
dists.insert(0, 'pip')  # let 'pip' be the first

for dist_name in dists:
    cmd = "pip install {0} -U".format(dist_name)
    print('#', cmd)
    os.system(cmd)