import urllib2
import urllib
import re

class NoRedirection(urllib2.HTTPErrorProcessor):
   	def http_response(self, request, response):
      		return response
    	https_response = http_response

def get_csrf():
	res1 = urllib2.urlopen("url here")
	nsid = re.search('nsid=(.*); Path', res1.info().getheader('Set-Cookie')).group(1)
	csrf = re.search('_csrf" value="(.*)" /><input type="hidden"', res1.read()).group(1).replace('&#x', '%').replace(';', '')
	return {'nsid': nsid, 'csrf': csrf}

def login_request(u, p):
	proxy_support = urllib2.ProxyHandler({"https": "http://127.0.0.1:8080"})
	opener = urllib2.build_opener(NoRedirection,proxy_support)
	urllib2.install_opener(opener)
	c = get_csrf()
	headers = {"Cookie": "nsid="+c['nsid']+"; login_email="+u, "Content-Type": "application/x-www-form-urlencoded"}
	opener.addheaders = [("Cookie", "nsid="+c['nsid']+ "; login_email="+ u), ("Content-Type", "application/x-www-form-urlencoded")]
	params = {'username': u, 'password': p, "_csrf": urllib.unquote(c['csrf']).decode('utf8'), 'submit.x' : 'Log in', 'type': '0'}	
	#print urllib.urlencode(params)
	res2 = opener.open("url here", urllib.urlencode(params))
	print(res2.info().getheader('Set-Cookie'))

if __name__ == "__main__":
	#for i in range(1,100):
	#	login_request('u', 'a'*i)
	login_request('username', 'password')

