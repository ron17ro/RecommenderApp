from boto.s3.connection import S3Connection
import os

KEYS = dict([
	('OpenWeatherMap',  os.environ.get('OpenWeatherMap')),
	('google_API',  os.environ.get('google_API')),
	('mailGun',  os.environ.get('mailGun')),
	('CommentEmail',  os.environ.get('CommentEmail'))

])
