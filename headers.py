import time

def set_cors_headers(response):
	response.headers.add_header("Access-Control-Allow-Origin", "*")


def set_cache_headers(response, cache_time):
	response.headers['Cache-Control'] = 'public, max-age=' + str(cache_time) + ', stale-if-error=604800, stale-while-revalidate=60'
	response.headers['Date'] = str(time.time())

def json(response):
	response.headers['Content-Type'] = 'application/javascript'
