#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_

from bs4 import BeautifulSoup
import re
import urllib.parse
class Analys(object):
    def _get_new_urls(self,url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,url,soup):
        data = {}

        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title_node.get_text()
        summery_node = soup.find('div',class_ = 'lemma-summary')
        data['abstract'] = summery_node.get_text()
        data['url'] = url
        return data

    def result(self,html_data,url):
        if html_data is None or url is None:
            return None
        soup = BeautifulSoup(html_data,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)
        return new_urls,new_data
