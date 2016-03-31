# -*- coding: utf-8 -*-

import os

try:
	import urlparse
except ImportError:
	import urllib.parse as urlparse


DEFAULT_ENV = 'MONGO_DATABASE_URL'

def config(env=DEFAULT_ENV, default=None):
	"""Returns configured DATABASE dictionary from MONGO_DATABASE_URL."""

	config = {}

	s = os.environ.get(env, default)

	if s:
		config = parse(s)

	return config


def parse(url):
	"""Parses a database URL."""

	config = {}

	url = urlparse.urlparse(url)

	# Remove query strings.
	path = url.path[1:]
	path = path.split('?', 2)[0]
	path = path.split("/", 1)

	# Update with environment configuration.
	config.update({
		'NAME': path[0],
		'USER': url.username,
		'PASSWORD': url.password,
		'HOST': url.hostname,
		'PORT': url.port,
		'COLLECTION': path[1] if len(path) > 1 else None,
	})

	return config
