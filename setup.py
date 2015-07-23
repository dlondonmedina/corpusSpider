try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = { 
	'description': 'Corpus Spider',
	'author': 'Dylan Medina',
	'url': '',
	'download_url':'',
	'author_email':'',
	'versiion':'0.1',
	'install_requires':['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'corpusSpider'
}

setup(**config)
