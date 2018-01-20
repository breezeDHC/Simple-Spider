#/usr/bin/env python3
#_*_ encoding:utf-8

import urlManager,output,downloader,analysis
class SpiderMain(object):
    def __init__(self):
        self.url = urlManager.UrlManager()
        self.downloader = downloader.Downloader()
        self.analys = analysis.Analys()
        self.output = output.Output()
    def craw(self,root_url):
            count = 1
            self.url.add_url(root_url)
            while self.url.has_url():
                try:
                    new_url = self.url.get_url()
                    print("craw %d (%s)" % (count,new_url))
                    html_data = self.downloader.get_htmlData(new_url)
                    urls,content = self.analys.result(html_data,new_url)
                    self.url.add_urls(urls)
                    self.output.collect(content)

                    if count == 10:
                        break

                    count = count + 1
                except:
                    print("craw %d fail" % count)
            self.output.make()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    ob_main = SpiderMain()
    ob_main.craw(root_url)
