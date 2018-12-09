from boto.s3.connection import S3Connection
import os

KEYS = dict([
	('OpenWeatherMap',  os.getenv('OpenWeatherMap')),
	('google_API',  os.getenv('google_API')),
	('mailGun',  os.getenv('mailGun')),
	('CommentEmail',  os.getenv('CommentEmail'))

])
