import urlparse
import urllib
import logging

from google.appengine.api.urlfetch import fetch
from google.appengine.api import memcache

CONTENT_API_HOST = 'content.guardianapis.com'

def content_id(url):
	parsed_url = urlparse.urlparse(url)
	return parsed_url.path

def read(content_id, params = None):
	client = memcache.Client()

	url = "http://%s%s" % (CONTENT_API_HOST, content_id)

	if params:
		url = url + "?" + urllib.urlencode(params)

	#logging.info(url)

	cached_data = client.get(url)

	if cached_data: return cached_data

	result = fetch(url)

	if not result.status_code == 200:
		logging.warning("Content API read failed: %d" % result.status_code)
		return None

	client.set(url, result.content, time = 60 * 15)

	return result.content

def search(query):
	url = "http://content.guardianapis.com/search?%s" % urllib.urlencode(query)

	cached_data = memcache.get(url)

	if cached_data:
		return cached_data

	result = fetch(url)

	if not result.status_code == 200:
		logging.warning("Failed to search API: %s" % url)
		return None
	
	memcache.set(url, result.content, time=60*3)
	return result.content

def response_ok(response):
	if not response:
		return False

	if not "response" in response:
		return False

	if not "status" in response["response"]:
		return False

	if not response["response"]["status"] == "ok":
		return False

	if not "content" in response["response"]:
		return False

	return True