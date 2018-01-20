#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

import urllib.request

class Downloader(object):
    def get_htmlData(self,url):
        if url is None:
            return None
        else:
            response = urllib.request.urlopen(url)
            if response.getcode() != 200:
                return None
            else:
                return response.read()
