#/usr/bin/env python3
#_*_ encoding:utf-8

class UrlManager(object):

    def __init__(self):
        self.old_url = set()
        self.new_url = set()
        
    def add_url(self,url):
        if url is None:
            return
        if url not in self.old_url and url not in self.new_url:
            self.new_url.add(url)
            
    def add_urls(self,urls):
        if len(urls) == 0 or urls is None:
            return 
        for url in urls:
            self.add_url(url)

    def has_url(self):
        if len(self.new_url) == 0:
            return False
        else:
            return True
    def get_url(self):
        url = self.new_url.pop()
        self.old_url.add(url)
        return url
