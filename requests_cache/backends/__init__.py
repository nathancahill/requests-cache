#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    requests_cache.backends
    ~~~~~~~~~~~~~~~~~~~~~~~

    Classes and functions for cache persistence
"""

from .base import BaseCache

registry = {
    'memory': BaseCache,
}
try:
    from .mongo import MongoCache
    registry['mongo'] = registry['mongodb'] = MongoCache
except ImportError:
    MongoCache = None
