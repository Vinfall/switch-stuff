#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Author: Vinfall
# License: AGPL
# Split Switch cheats into Yuzu-supported formats
# Prerequisites: remove unwanted cheats and trailing spaces
# Usage: change bid & version, run the program et voila!

import os

build_id = '38F59CBDA2EB9C44'
version = '[1.3.0] '

with open(build_id + '.txt', 'r', encoding='utf-8') as f:
    # Read cheats one by one
    cheats = f.read().split('\n\n')
for cheat in cheats:
    if len(cheat) > 1:
        # Cheat name
        name = cheat.splitlines()[0]
        # Sanity check
        basename = ''.join(x for x in name[1:-1]
                           if (x.isalnum() or x in "._-+ ()[]×"))
        dirname = version + basename
    if not os.path.exists(dirname):
        # Create subdirectory before creating sub-subdirectory
        os.mkdir(dirname)
        # Do not scape '
        os.mkdir(dirname + '\cheats\\')
    with open(dirname + '\cheats\\' + build_id + '.txt', 'w',
              encoding='utf-8') as f:
        f.write(cheat)
        f.close()
print('Remember to delete cheat info dir')

