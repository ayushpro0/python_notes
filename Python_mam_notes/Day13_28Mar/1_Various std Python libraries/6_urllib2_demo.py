
import urllib
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()
print(html)



"""
req = urllib2.Request('http://python.org')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
"""

"""
This module provides a high-level interface for fetching data across the World Wide Web.
In particular, the urlopen() function is similar to the built-in function open(),
but accepts Universal Resource Locators (URLs) instead of filenames.
Some restrictions apply — it can only open URLs for reading, and no seek operations are available.


proxies = {'http': 'http://www.someproxy.com:3128'}
filehandle = urllib.urlopen(some_url, proxies=proxies)


>set HTTP_proxy=http://ptbc1.persistent.co.in:8080/
>set HTTPS_proxy=https://ptbc1.persistent.co.in:8080/

"""





