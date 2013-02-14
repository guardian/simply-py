from google.appengine.ext import ndb

class Configuration(ndb.Model):
	key = ndb.StringProperty()
	value = ndb.StringProperty()
