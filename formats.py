
def jsonp(request, json_string):
	if request.get("callback"):
        return "%s(%s)" % (self.request.get("callback"), json_string)
    return json_string
