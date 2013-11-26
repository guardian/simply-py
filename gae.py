import os

def is_development():
	return os.environ['SERVER_SOFTWARE'].startswith('Development')