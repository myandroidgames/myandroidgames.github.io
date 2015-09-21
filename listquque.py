#! /usr/bin/env python

import os
QUEUE_PATH = 'apps/queue'
lst = os.listdir(QUEUE_PATH)
for item in lst:
    print item
