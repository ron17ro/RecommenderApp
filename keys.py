from boto.s3.connection import S3Connection
import os

KEYS = dict([
	('OpenWeatherMap',  S3Connection(os.environ.get('OpenWeatherMap'))),
	('google_API',  S3Connection(os.environ.get('google_API'))),
	('mailGun',  S3Connection(os.environ.get('mailGun'))),
	('CommentEmail',  S3Connection(os.environ.get('CommentEmail')))

])
