#!/usr/bin/env python3 
#_*_ encoding:utf-8 _*_

class Output(object):
    def __init__(self):
        self.data=[]

    def collect(self,content):
        if content is None:
            return 
        self.data.append(content)
    def make(self):
        f = open('output.html','w')
        f.write('<html>')
        f.write("<head><meta http-equiv='content-type' content='text/html;charset=utf-8'></head>")
        f.write('<body>')
        f.write('<table>')
        for x in self.data:
            f.write('<tr>')
            f.write('<td>%s</td>' % x['url'])
            f.write('<td>%s</td>' % x['title'])
            f.write('<td>%s</td>' % x['abstract'])
            f.write('</tr>')
        f.write('</table>')
        f.write('</body>')
        f.write('</html>')
        f.close()
