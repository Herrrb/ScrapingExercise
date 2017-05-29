# -*- encoding:utf-8 -*-
import requests
import lxml.html
import re
s = requests.session()

def parse_form(html):
	tree = lxml.html.fromstring(html)
	data = {}
	for e in tree.cssselect('form input'):
		if e.get('name'):
			data[e.get('name')] = e.get('value')
	return data



html = s.get('http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2F202.117.124.85%2Flogin%2F').content

data = parse_form(html)

username = raw_input (unicode('请输入学号：','utf-8').encode('gbk'))
password = raw_input (unicode('请输入密码：','utf-8').encode('gbk'))
data['username'] = username
data['password'] = password

response = s.post('http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2F202.117.124.85%2Flogin%2F',data=data)
buf = response.content
# f = open('c:/python27/testlogin.txt','w')
# f.write(buf)
# f.close()

tree = lxml.html.fromstring(buf)
name = tree.cssselect('li.nav-item')[0]
name = name.text_content()
times = tree.cssselect('div.huge')[0]
times = times.text_content()
print re.findall('^(.*?)\(',name)[0]
print "您的有效打卡次数为".decode('utf-8').encode('gbk'),times,"次".decode('utf-8').encode('gbk')