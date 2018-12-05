from boto.s3.connection import S3Connection
import os

KEYS = dict([
	('OpenWeatherMap',  S3Connection(os.environ['OpenWeatherMap'])),
	('google_API',  S3Connection(os.environ['google_API'])),
	('mailGun',  S3Connection(os.environ['mailGun'])),
	('CommentEmail',  S3Connection(os.environ['CommentEmail']))

])
