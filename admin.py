import webapp2
import jinja2
import os
import json
import logging
from urllib import quote, urlencode
from google.appengine.api import urlfetch

import configuration

from models import Configuration

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), "templates")))

class ConfigurationPage(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('admin/configuration.html')
		
		template_values = {}

		template_values['configuration'] = Configuration.query()

		self.response.out.write(template.render(template_values))

	def post(self):
		key = self.request.POST['key']
		value = self.request.POST['value']
		map(lambda x: logging.info(x), [key, value])

		configuration.create(key, value)

		return webapp2.redirect('/admin/configuration')
		

app = webapp2.WSGIApplication([('/admin/configuration', ConfigurationPage)],
                              debug=True)