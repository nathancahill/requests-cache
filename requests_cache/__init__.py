#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    requests_cache
    ~~~~~~~~~~~~~~

    Transparent cache for ``requests`` library with persistence and async support

    Just write::

        import request_cache
        request_cache.configure()

    And requests to resources will be cached for faster repeated access::

        import requests
        for i in range(10):
            r = requests.get('http://httpbin.org/redirect/5')
        # will took  approximately 5 seconds instead 50


    :copyright: (c) 2012 by Roman Haritonov.
    :license: BSD, see LICENSE for more details.
"""
from core import configure, clear, redo_patch, undo_patch, get_cache